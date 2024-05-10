const MILLION = 1_000_000;
const NANO_SECOND = 10 ** -9;

class Redis {
    constructor() {
        this.throughput = 10 * MILLION;
        this.speed = 1 / (100 * NANO_SECOND);
    }
}