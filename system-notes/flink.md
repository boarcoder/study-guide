# Netflix 2017 Numbers - Flink with Elasticsearch sink

## Raw Numbers

1.3 trillion, 1.3E12(trillion) events per day
3 PB, 3E15 byte incoming data
9 PB, 9E15 byte outgoing data
99% availability
4k kafka brokers on 50 clusters (80 kafka/cluster)
200 flink job data streams
3700 flink containers
1400 nodes, 22k cpu cores (16 cores/node)

### Breakdown for Flink QPS:

- 15 million, 1.5E7 events/second
- 1.5E7 events/1400 nodes = 10k event velocity (events/s)/node
- SIMPLE: 
    - 1E7 events/sec
    - 1E4 (10,000) (event/s)/ flink node

### Estimation reminders:
- 100k seconds per day (estimate)

--
Other use case:
Sliding window user sesson management
2-24 hour session
1 billion 1E11 eevnts per day with 100GB job state in flink
Late or out-of-order events supported

---
## Conclusions

- QPS node: 10k per flink with DB sink (elasticsearch)
- QPS total: 1.5E7, increased horizontal, per node.
- RTT: 2 minutes time to process.
- Machine count: Total QPS/10k.
- Machine spec: 16 cores, 100GB RAM, 1TB NVME.

Note 1: RTT according to gpt is around 200ms, but exactly-once increases this.
The netflix scenario includes data processing that increased the lag to 1-2 minutes.

Note 2: QPS can be increased if the SINK is not a database. Netflix is including the QPS to process, insert into Elasticsearch, at least once per message.
