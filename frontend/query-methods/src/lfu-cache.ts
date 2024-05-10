type CacheItem = {
    value: number;
    freq: number
}

class LFUCache {
    private cache = new Map<number, CacheItem>();
    private capacity: number = 0;

    private frequencyHash = {0: new Set()};
    private minFreq: number = 0;
    
    constructor(capacity: number) {
        this.capacity = capacity;
    }

    /*
    1. If the key dont exist, return -1
    2. The key exists
    3. Delete the old freq_map of key
    4. Increase frequency
    5. If the freq_map does not have new frequency, create it
    6. Increase element_map of key freq
    7. Add key to freq_map
    8. Update min_freq. The only time we update, is if it is 0, as we are getting and adding a freq=1
    9. Return value
    */
    get(key: number): number {
        if (! this.cache.has(key)) return -1;

        const item: CacheItem = this.cache.get(key);
        this.frequencyHash[item.freq].delete(key);
        item.freq += 1;
        if (! this.frequencyHash[item.freq]) {
            this.frequencyHash[item.freq] = new Set();
        }
        this.frequencyHash[item.freq].add(key);
        this.cache.set(key, item);

        if (this.frequencyHash[this.minFreq].size == 0) this.minFreq += 1;

        return item.value;
    }

    /*
    1. If this 
    */

    put(key: number, value: number): void {
        if (this.cache.has(key)) {
            const item: CacheItem = this.cache.get(key);
            this.frequencyHash[item.freq].delete(key);
            item.freq += 1;
            item.value = value;
            this.cache.set(key, item);

            if (! this.frequencyHash[item.freq]) this.frequencyHash[item.freq] = new Set();
            this.frequencyHash[item.freq].add(key);

            if (this.frequencyHash[this.minFreq].size == 0) this.minFreq += 1;

            return;
        }

        if (this.cache.size == this.capacity) {
            const keyToEvict = this.frequencyHash[this.minFreq].keys().next().value;
            this.frequencyHash[this.minFreq].delete(keyToEvict);
            this.cache.delete(keyToEvict);
        }

        const item: CacheItem = {value, freq: 1};
        this.cache.set(key, item);
        if (! this.frequencyHash[item.freq]) {
            this.frequencyHash[item.freq] = new Set();
        }
        this.frequencyHash[item.freq].add(key);
        this.minFreq = item.freq;
    }
}
