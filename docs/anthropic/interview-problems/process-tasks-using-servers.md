# Process Tasks Using Servers

- LeetCode: [1882. Process Tasks Using Servers](https://leetcode.com/problems/process-tasks-using-servers/)
- Category: `Role-aligned proxy`
- Why it is here: this is the closest LeetCode-style proxy for allocation systems and fleet scheduling.

## Framework Classification

- Input structure: servers with weights and tasks arriving over time
- Output asks for assignment of tasks to resources
- Repeated operation: choose the best free server, or wait for the next release
- Remembered state: free-server heap and busy-server heap

## Pattern Choice

- Primary: two-heap scheduler
- Secondary: event simulation

## Invariant

One heap holds all free servers ordered by scheduling priority, and the other holds busy servers ordered by release time.

## Skeleton Plan

1. Put all servers into a free heap by `(weight, index)`.
2. As time advances, move completed servers back into the free heap.
3. If no server is free, jump to the next release time.
4. Assign the next task to the best available server.

## Python Solution

```python
import heapq


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        answer = []
        time = 0

        for i, duration in enumerate(tasks):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                _, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))

            if not free:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    _, weight, idx = heapq.heappop(busy)
                    heapq.heappush(free, (weight, idx))

            weight, idx = heapq.heappop(free)
            answer.append(idx)
            heapq.heappush(busy, (time + duration, weight, idx))

        return answer
```

## Common Pitfalls

- Using one heap instead of separating free and busy resources
- Failing to advance time when no server is available
- Getting heap ordering wrong for tie-breaking

## Related Docs

- [Algorithm Framework](../algorithm-framework.md)
