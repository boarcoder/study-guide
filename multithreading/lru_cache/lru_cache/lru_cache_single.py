class LRUCacheSingle:
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

import unittest
import logging as log

class TestLRUCacheSingle(unittest.TestCase):
    def test_lru_can_add(self):
        lru = LRUCacheSingle(5)
        for i in range(10):
            lru.set(i, f'value for {i}')

        expected = {
            5: 'value for 5',
            6: 'value for 6',
            7: 'value for 7',
            8: 'value for 8',
            9: 'value for 9',
        }
        self.assertDictEqual(expected, lru.dic)

if __name__ == '__main__':
    unittest.main()