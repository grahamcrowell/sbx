# CAP

## Consistency

### Weak Consistency

- writes are not guaraneed
- realtime
- memcached

### Eventual Consistency

- concurrent reads may return inconsistent results
- writes are guaranteed
- is [BASE](base.md)

### Strong Consistency

- is [ACID](acid.md)

## Availability

### High Availability

- every request gets a response
- allows for eventual consistency

## Partition Tolerence

- Removing a partition does not cause data loss (replication)

