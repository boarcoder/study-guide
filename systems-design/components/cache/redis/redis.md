# Redis

## Classification

- Throughput: 10 million QPS
- Speed: 100 nano seconds


## Inputs

Every component should declare inputs like a function, if they are relevant to it. For example:

- QPS
- Read Mbps
- Write Mbps
- Storage GB
- Min latency

## Outputs

Component should be able to calculate when relevant:

- RTT: Round Trip Time (Staff)
- Machine Count (Sr)
- Active/active or active/passive (Sr)
- Storage requirements (Sr)