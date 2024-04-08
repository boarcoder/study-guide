from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from concurrent.futures import as_completed
from lru_cache.lru_cache_single import LRUCacheSingle
import time

'''
Now let's give a best-case scenario for using a multi-threaded LRU cache.
1. We will set the cache with keys 1-100. (capacity of 100)
2. We will purposefully cause as many waits for cache access as possible:
  - repeatedly attempt to change the value of keys, 1-n, where n is shards
  or another number that distributes the key access (not to just 1 shard)
  if multi-threaded were to be used.
3. Get process time for single vs multi threaded.

Expectation: Multi-threaded LRU cache should be faster, as atomic access,
which is a wait in que to modify a key of global dict, should be split to
sharded LRU caches on their own threads.
'''
# Even though shards aren't used on single, we will still compare the same keys
LRU_SHARDS = 4
LRU_CAPACITY = 10
SET_KEY_ITERATIONS = 10**6

def initialize_lru_keys(lru, capacity):
    for i in range(capacity):
        lru.set(i, f'initial value for {i}')

def set_key_dist(lru, iterations, num_shards):
    for _ in range(iterations):
        for i in range(num_shards):
            lru.set(i, f's-{i}')
            
lru = LRUCacheSingle(LRU_CAPACITY)
initialize_lru_keys(lru, LRU_CAPACITY)

def threadedFunction(i):
    set_key_dist(lru, SET_KEY_ITERATIONS, LRU_SHARDS)
    return f'result of future i: {i}'

print('Initialize the LRU cache with keys 1-100')
print('process time:', time.process_time())
print('-------------------------------')
print('starting ProcessPoolExecutor')
with ProcessPoolExecutor(max_workers=4) as executor:
    future_list = [executor.submit(threadedFunction, i) for i in range(100)]
print('process time:', time.process_time())