class LFUCache {
    private cache: any;
    private capacity: number;

    private frequencyHash = {0: new Set()};
    private minFreq: number = 0;

    constructor(capacity: number) {
        this.cache = new Map();
        this.capacity = capacity;
    }

    get(key: number): number {
        if(!this.cache.has(key)) return -1
        
        let { data, times } = this.cache.get(key)
        this.frequencyHash[times].delete(key);
        times++
        this.cache.set(key, { data, times })
        
        if (!this.frequencyHash[times]) {
            this.frequencyHash[times] = new Set();
        }
        this.frequencyHash[times].add(key)

        if (this.frequencyHash[this.minFreq].size == 0) this.minFreq += 1;

        return data;
    }

    put(key: number, value: number): void {
        if(this.cache.has(key)){
            let { times } = this.cache.get(key)
            this.frequencyHash[times].delete(key)
            
            times++
            this.cache.set(key, { data: value, times: times })
            if (! this.frequencyHash[times]) {
                this.frequencyHash[times] = new Set();
            }
            this.frequencyHash[times].add(key)

            if (this.frequencyHash[this.minFreq].size == 0) this.minFreq += 1;          
            return
        } 

        if (this.cache.size == this.capacity) {
            const keyToEvict = this.frequencyHash[this.minFreq].keys().next().value;
            this.frequencyHash[this.minFreq].delete(keyToEvict);
            this.cache.delete(keyToEvict);
        }
        this.cache.set(key, {data: value, times: 1});
        
        if (!this.frequencyHash[1]) {
            this.frequencyHash[1] = new Set();
        }
        this.frequencyHash[1].add(key);
        this.minFreq = 1;
    }
}
