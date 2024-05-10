# Load Balancer

### Intro

Load balancers are a reverse proxy between application layers.

Locally, keep state of health of server, via heartbeats.

- Number of connections open
- Load
- Last heartbeat
- Local

Route traffic to each server based on routing policies.

----

### Routing policies

1. Least connections
2. Least response time
3. Weighted round robin (In order of list, we apply requests, but weight on server capacity)
4. Hashing - based on request contents (used for partitioning)

----

### Layer 4 vs Layer 7 (L4 vs L7) Load Balancing

#### Layer 4

Requests are routed based on details exposed by layer

- Source IP
- Destination IP
- Ports in header

*+ Computationally faster*

#### Layer 7

Requests are routed based on header contents

- More flexible
- Hash on more relevant information

## Product Selection

### nginx plus

Solution to route requests to different server IP

```
+ session persistence
+ active health checks
+ dynamic hot reconfigure host groups
```

### DNS

A url resolves to a number of IP addresses

```
+ Don't need separate machine
- Less customizable
```

## L4 vs L7???

<!-- 
## Function: RTT

Example inputs:
100  TPS Write
100k TPS Read
Read-imbalance: 75% are reads of same url from last week
100 characters per url on average
5 year retention policy
3-4 9 availability (99.999_)
```
def RTT(QPS):
    rtt = 

    return rtt

``` -->