from multi_sampling import LRUCacheMultithread
from lru_cache_single import LRUCacheSingle
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import time

'''
This would be the setup when our app initializes
'''
SHARD_COUNT = 4
CAPACITY = 16
lru = LRUCacheMultithread(shard_count=SHARD_COUNT, capacity=CAPACITY)
    
# with ThreadPoolExecutor(max_workers=10):

'''
This function runs in a thread.
'''
# def accessCacheInThread(lru_cache, thread_number):
#     # print('checking thread-safe LRU cache.')
#     # print('setting cache initial values.')
#     for i in range(16):
#         lru_cache.set(i, f'value-{i}')
#     for i in range(16):
#         lru_cache.get(i)

#     for _ in range(1000):
#         for i in range(10,20):
#             lru_cache.set(i, f'changed value on {i}')
    
#     time.sleep(5)
#     return f'completed thread_number {thread_number}'


# with ThreadPoolExecutor(max_workers=5) as executor:
#     future_list = [executor.submit(accessCacheInThread, lru, i) for i in range(20)]

#     for fut in as_completed(future_list):
#         print(f'result of future:', fut.result())

# print('process time:', time.process_time())

'''
Now let's give a best-case scenario for using a multi-threaded LRU cache.
1. We will set the cache with keys 1-100. (capacity of 100)
2. We will purposefully cause as many wait for atomic access as possible:
  - repeatedly attempt to change the value of key 50.
3. Time single vs multi threaded.
Expectation: Multi-threaded LRU cache should be faster, as atomic access,
which is not a lock but a wait in line to modify a key, should be split to
sharded LRU caches (dict) on their own threads.
'''
LRU_CAPACITY = 100
SET_KEY_ITERATIONS = 1_000_000
def initialize_lru_keys(lru, capacity):
    for i in range(capacity):
        lru.set(i, 'initial value for {i}')

def set_key_n_times(lru, n, key, value):
    for i in range(n):
        lru.set(key, value)

# Single thread
lru = LRUCacheSingle(LRU_CAPACITY)
initialize_lru_keys(lru, LRU_CAPACITY)
set_key_n_times(SET_KEY_ITERATIONS)



