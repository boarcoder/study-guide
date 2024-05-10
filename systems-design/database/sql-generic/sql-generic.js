const MILLION = 1_000_000;
const MS = 10 ** -3;

class SQLGeneric {
    constructor() {
        this.throughput = 1000; // QPS possible to serve.
        this.speed = 1 / MS; // Average time to serve 1 request.
        this.latency = ; // Time
    }

    getMachineCount(qpsRequired) {
        return qpsRequired / this.throughput;
    }

    getRoundTripTime() {

    }
}