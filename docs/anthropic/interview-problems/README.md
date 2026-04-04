# Anthropic Interview Problems

This folder is the Anthropic-specific version of what we did for Anduril.

It is not an official Anthropic question bank. It is a curated problem set built from:

- public interview anecdotes that repeatedly mention practical crawler/concurrency tasks and progressive in-memory system design
- Anthropic's current compute-capacity role language around observability, utilization, allocation, and fleet efficiency

## Public Signals

- Strongest recurring public signal: crawler or scraper style coding with concurrency follow-ups
- Another recurring signal: progressive CodeSignal-style in-memory system design and extension
- Role-aligned proxy themes: scheduling, dependency graphs, caches, interval reasoning, and telemetry/stateful service design

## Source Links

- [Anthropic Compute Capacity role](https://job-boards.greenhouse.io/anthropic/jobs/5126702008?gh_jid=5126702008)
- [Glassdoor Anthropic interviews](https://www.glassdoor.com/Interview/Anthropic-Sales-Development-Manager-Interview-Questions-EI_IE8109027.0%2C9_KO10%2C35.htm)
- [Reddit thread mentioning practical Anthropic CodeSignal](https://www.reddit.com/r/leetcode/comments/1roiidg/anthropic_fde_interview/)

## How To Read This Set

- `Public-signal` problems are the closest public matches I found.
- `Proxy` problems are not reported exact questions, but they map well to the role and interview shape.
- Each note includes framework classification, invariant, skeleton plan, and a Python reference solution.

## Problem Set

### Public-Signal Closest Matches

- [Web Crawler](./web-crawler.md)
- [Web Crawler Multithreaded](./web-crawler-multithreaded.md)
- [Design In-Memory File System](./design-in-memory-file-system.md)
- [Time Based Key-Value Store](./time-based-key-value-store.md)

### Role-Aligned Proxies

- [LRU Cache](./lru-cache.md)
- [Course Schedule](./course-schedule.md)
- [Course Schedule II](./course-schedule-ii.md)
- [Single-Threaded CPU](./single-threaded-cpu.md)
- [Process Tasks Using Servers](./process-tasks-using-servers.md)
- [Merge Intervals](./merge-intervals.md)

## Why These Problems

This set is trying to train the actual muscles that seem relevant here:

- graph traversal over real-world state spaces
- concurrency-aware design
- stateful in-memory service modeling
- scheduling and resource allocation
- dependency management
- interval reasoning
- cache and storage behavior

## Related Docs

- [Algorithm Framework](../algorithm-framework.md)
- [Python Concepts](../python-concepts.md)
- [Level One Problems](../level-one-problems.md)
- [UV Test Harness](../test-harness.md)
