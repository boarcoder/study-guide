
## Hacks

- Auto sharding
- Auto load balaning
- Server at load will auto redistribute load as such.
- Consistent hashing for nodes.
- Global tables replication for regions.
- multiple Availability Zones in each region.

On-demand pricing or you can pay per hour.

Read Capacity Unit (RCU)
$1.12 per million reads (4KB each)
Provides one strongly consistent read per second for items up to 4KB, or two eventually consistent reads per second.

Write Capacity Unit (WCU)
$5.62 per million writes (1KB each)
Provides one write per second for items up to 1KB.

An AWS shard supports 1,000 read capacity units and 1,000 write capacity units. This means that a single shard can support 4MB of reads per second and 1MB of writes per second

## When DO NOT use:

1. Complex joins and subqueries
2. Multi-table transactions (ddb limit on number of items)
3. Data model complexity - too many GSI and LSI hard to manage?

## Identifiers

- Table: Collections of related data
- Items (Rows): Records with a unique pkey.
- Attributes (Cols): Data fields

As with other NOSQL, we don't care about missing or empty columns.

## Lookup Keys

partition_key: physical node hardware location of storage.
sort_key (optional): B-Key index in memory for RANGE or SORT queries.
primary_key: partition_key:sort_key

### Examples

partition_key: chat_id, user_id
sort_key: message_id, order_id, post_id
(these sort keys are monotonic increasing examples)

## Sort

GSI (global secondary index): sort by sort_key, but on all partitions instead of 1 partition. GSI creates a secondary partition and replica which requires more storage to duplicate this!

LSI (local secondary index): partition_key:sort_key(for_other_index)

## Transactions

Allowed

## Consistency - Eventual Read Allowed 

SINGLE leader node. Consistent hashing on partition_key.

SLOPPY QUORUM - Replica down, we allow writes to the leader regardless of inconsistencies.

Therefore, EVENTUAL consistency is allowed to occur and give stale data in reads, if we read from non-leader node. This is allowed.

## Consistency - Strong Read Allowed 

SINGLE leader node

We only allow reads from leader node. No replication lag for reads.

Consumes more read capacity (1 RCU per 4KB) and may have higher latency.

Scale may be decreased !

## Need read-heavy low latency - DAX

Read/write through caching in front of dynamodb. Microsecond response times. In most cases you want to enable DAX instead of using REDIS.

## DDB Streams - Triggers

Table modifications can trigger lambda or other things.
