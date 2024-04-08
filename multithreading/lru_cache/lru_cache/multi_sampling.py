'''
Problem: locks are causing threads to wait too long.
Solution - Shard LRU Cache:
To decrease locks, we provide shards of lru cache that threads can use.
'''
class LRUCacheMultithread:
    def __init__(self, shard_count=4, capacity=100):
        self.shard_count = shard_count
        self.capacity = capacity
        self.shard_list = []
        if not self.shard_list:
            self.setup_shard_cache_list()
    
    '''
    Shard the cache based on the key grouping (A-F,G-J,K-P...) and get from appropriate 
    ShardLRUCache object in memory.
    For simple algorithm we will just use hash on key value modulo by threads.
    '''
    def setup_shard_cache_list(self):
        shard_cap = self.capacity // self.shard_count
        for _ in range(self.shard_count):
            s = self.ShardLRUCache(capacity=shard_cap)
            self.shard_list.append(s)

    def get(self, key):
        shard_cache = self._get_shard_cache(key)
        return shard_cache.get(key)
    
    def set(self, key, value):
        shard_cache = self._get_shard_cache(key)
        return shard_cache.set(key, value)
    
    def _get_shard_cache(self, key):
        hash_int = hash(key)
        shard_thread = hash_int % self.shard_count
        return self.shard_list[shard_thread]
        
    class ShardLRUCache:
        def __init__(self, capacity=100):
            self.capacity = capacity \
                if capacity is not None \
                else float('inf')
            self.dic = {}
            
        def get(self, key):
            res = self.dic.get(key)
            if res is not None:
                del self.dic[key]
                self.dic[key] = res
            return res
        
        def set(self, key, value):
            cached_res = self.get(key)
            if cached_res is None and len(self.dic) >= self.capacity:
                for key in self.dic:
                    del self.dic[key]
                    break
            self.dic[key] = value
            return value