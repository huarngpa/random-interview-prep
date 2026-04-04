# Single-Threaded CPU

- LeetCode: [1834. Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/)
- Category: `Role-aligned proxy`
- Why it is here: this is a clean scheduling problem for queueing, prioritization, and utilization reasoning.

## Framework Classification

- Input structure: tasks with enqueue times and processing times
- Output asks for the execution order
- Repeated operation: choose the best available task at each time
- Remembered state: min-heap of runnable tasks

## Pattern Choice

- Primary: sort plus heap scheduling
- Secondary: simulation over time

## Invariant

The heap always contains exactly the tasks that have arrived but not yet been processed.

## Skeleton Plan

1. Sort tasks by arrival time.
2. Advance time while pushing newly available tasks into a heap.
3. Pop the shortest available task, breaking ties by index.
4. If the heap is empty, jump time forward.

## Python Solution

```python
import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        indexed = sorted((enqueue, process, i) for i, (enqueue, process) in enumerate(tasks))
        answer = []
        heap = []
        time = 0
        i = 0

        while i < len(indexed) or heap:
            if not heap and time < indexed[i][0]:
                time = indexed[i][0]

            while i < len(indexed) and indexed[i][0] <= time:
                enqueue, process, idx = indexed[i]
                heapq.heappush(heap, (process, idx))
                i += 1

            process, idx = heapq.heappop(heap)
            time += process
            answer.append(idx)

        return answer
```

## Common Pitfalls

- Advancing time incorrectly when no tasks are available
- Forgetting tie-breaking by original index
- Confusing this with interval overlap instead of event-driven scheduling

## Related Docs

- [Algorithm Framework](../algorithm-framework.md)
