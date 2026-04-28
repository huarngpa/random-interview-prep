# Design Numbers Cheat Sheet

This is the tiny set of numbers worth keeping in your head for system design interviews.

The goal is not exactness.

The goal is:

- fast back-of-the-envelope math
- order-of-magnitude sanity checks
- sounding grounded without overfitting to trivia

## 1. Time And Throughput Conversions

- `1 minute = 60 seconds`
- `1 hour = 3,600 seconds`
- `1 day = 86,400 seconds`

Useful request-rate anchors:

- `1 million / day ≈ 11.6 QPS`
- `10 million / day ≈ 116 QPS`
- `100 million / day ≈ 1,160 QPS`
- `1 billion / day ≈ 11,600 QPS`

Quick rule:

- `daily volume / 100,000 ≈ rough QPS`

Not exact, but good enough for fast thinking.

## 2. Storage Math

Core formula:

```text
storage per second = QPS * payload size
storage per day = QPS * payload size * 86,400
```

Good anchors:

- `1 KB * 1,000 writes/sec ≈ 1 MB/sec`
- `1 MB/sec ≈ 86.4 GB/day`
- `10 MB/sec ≈ 864 GB/day`

Very useful shortcut:

- `1,000 writes/sec * 1 KB ≈ 86 GB/day`
- `1,000 writes/sec * 10 KB ≈ 864 GB/day`

## 3. Network Bandwidth

- `1 byte = 8 bits`
- `1 Gbps ≈ 125 MB/sec`
- `10 Gbps ≈ 1.25 GB/sec`
- `100 Gbps ≈ 12.5 GB/sec`

This helps when someone says:

- "the network is 10 Gbps"

and you want to reason in payload sizes.

## 4. Latency Ladder

Do not memorize exact values. Memorize the shape:

- CPU cache: `~1 ns`
- RAM: `~100 ns`
- SSD: `~100 µs`
- HDD seek: `~1-10 ms`
- in-region network RPC: `~0.5-2 ms`
- cross-region network: `~50-100+ ms`

What this teaches:

- local memory is much cheaper than disk
- disk is much cheaper than cross-region round trips
- chatty remote calls are dangerous

## 5. Availability "Nines"

- `99%` = about `3.65 days/year`
- `99.9%` = about `8.76 hours/year`
- `99.99%` = about `52.6 minutes/year`
- `99.999%` = about `5.26 minutes/year`

This is useful when discussing:

- SLA / SLO expectations
- whether a design needs failover, buffering, or degraded mode

## 6. Replica / Capacity Thinking

You do not need fixed numbers here.

Just remember the pattern:

- peak QPS is what matters, not average QPS
- write amplification matters
- replicas improve read scale, but not free write scale
- secondary indexes and projections multiply storage and write cost

## 7. Caches And Search

Useful reminders:

- cache hit rate matters more than "we have a cache"
- search indexes are read-optimized copies, not source of truth
- projections and materialized views trade write complexity for read simplicity

## Tiny Worked Examples

### Example 1: Event Volume

If the system receives:

- `5,000 events/sec`
- `2 KB` each

Then:

- throughput is about `10 MB/sec`
- daily storage is about `864 GB/day`

### Example 2: Dashboard Stream

If `20,000 events/sec` arrive and each is `10 KB`:

- that is about `200 MB/sec`
- which is above `1 Gbps`

So now network and partitioning are very real concerns.

### Example 3: Daily To QPS

If you expect `50 million requests/day`:

- `50,000,000 / 86,400 ≈ 579 QPS`

That is not enormous by backend standards, which changes the architecture conversation.

## Best 3 To Truly Memorize

If you only keep three things:

1. `1 day = 86,400 seconds`
2. `1 Gbps ≈ 125 MB/sec`
3. the `99.9 / 99.99 / 99.999` downtime table

## How To Use These In Interviews

Say:

- "Let me do rough math."
- "This is back-of-the-envelope."
- "We’re in the hundreds of MB/sec range, not tens."
- "This looks like hundreds of QPS, not tens of thousands."

That sounds better than pretending to know exact numbers from memory.
