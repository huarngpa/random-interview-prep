# Single-Threaded CPU

- LeetCode: [1834. Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/)
- Why It Is Likely: this fits Anduril's heap taste extremely well. It is a scheduler problem where ordering, availability, and priority all matter at once.

## Pattern Family

- heap scheduling
- event-driven simulation

## Framework Classification

- Input structure: tasks with enqueue time and duration
- Output asks for the execution order
- Repeated operation: pick the best currently available task
- Hidden structure: one sorted arrival stream plus one heap of runnable work

## Principle To Internalize

Do not simulate every unit of time.

Think in events:

- tasks arrive
- CPU becomes free

The heap is the runnable frontier.

The sorted list is the arrival stream.

## Solving Walkthrough

1. Sort tasks by enqueue time.
2. Advance time to the next interesting event.
3. Push all tasks that have arrived into a heap.
4. Pop the shortest available task, breaking ties by index.
5. If no task is available, jump time forward to the next arrival.

## Python Solution

```python
import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        indexed = sorted((enqueue, processing, i) for i, (enqueue, processing) in enumerate(tasks))
        heap = []
        answer = []
        time = 0
        i = 0

        while i < len(indexed) or heap:
            if not heap and time < indexed[i][0]:
                time = indexed[i][0]

            while i < len(indexed) and indexed[i][0] <= time:
                enqueue, processing, idx = indexed[i]
                heapq.heappush(heap, (processing, idx))
                i += 1

            processing, idx = heapq.heappop(heap)
            time += processing
            answer.append(idx)

        return answer
```

## Complexity

- Time: `O(n log n)`
- Space: `O(n)`

## Historical Connection

This is a likely next-cycle successor to:

- `Find Median from Data Stream`
- `Merge k Sorted Lists`

The shared principle is maintaining the next best candidate under changing conditions.
