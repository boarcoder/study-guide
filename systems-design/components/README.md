# Components - Systems Design

- Each page will contain a common component, such as database, load balancer, memcache
- The goal is that you can pull a given component, and apply the detailed step-by-step to that component on your diagram

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