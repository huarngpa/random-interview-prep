# Process Tasks Using Servers

- LeetCode: [1882. Process Tasks Using Servers](https://leetcode.com/problems/process-tasks-using-servers/)
- Why It Is Likely: this is one of the strongest scheduler/allocation proxies for Anduril's historical taste. It feels operational and realistic without requiring a company-specific domain.

## Pattern Family

- two-heap scheduler
- resource allocation over time

## Framework Classification

- Input structure: servers with weights and tasks arriving over time
- Output asks for assignment decisions
- Repeated operation: move resources between free and busy states
- Hidden structure: the problem is really about the frontier of available servers

## Principle To Internalize

Use one heap for:

- who is currently free and best to choose

and a second heap for:

- who is currently busy and when they return

This is a classic "free pool / busy pool" systems pattern.

## Solving Walkthrough

1. Put all servers into a free heap keyed by `(weight, index)`.
2. Track busy servers in a heap keyed by `(release_time, weight, index)`.
3. Before assigning each task, free every server whose release time has arrived.
4. If no server is free, jump time to the next release.
5. Assign the task to the best free server and move it into the busy heap.

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

## Complexity

- Time: `O((n + m) log n)`
- Space: `O(n)`

## Historical Connection

This generalizes the same instincts found in:

- `Find Median from Data Stream`
- `Merge k Sorted Lists`

but in a more systems-flavored scheduling context.
