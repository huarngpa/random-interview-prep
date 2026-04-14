# Meeting Rooms II

- LeetCode: [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
- Why It Is Likely: this is a very clean interval-plus-heap problem, which fits the Anduril history of interval reasoning and scheduler-style ordering.

## Pattern Family

- intervals
- sort + heap

## Framework Classification

- Input structure: meeting intervals
- Output asks for the minimum number of simultaneous resources
- Repeated operation: reclaim ended intervals and reuse their resources
- Hidden structure: start times define event order, end times define resource release

## Principle To Internalize

This is not just interval merging.

It is:

- how many overlapping intervals exist at peak?

The heap tracks the rooms currently occupied by their end times.

## Solving Walkthrough

1. Sort meetings by start time.
2. Keep a min-heap of current meeting end times.
3. Before adding a new meeting, pop all rooms whose end time is at or before the start.
4. Push the new meeting end time.
5. Track the maximum heap size.

## Python Solution

```python
import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        heap = []
        best = 0

        for start, end in intervals:
            while heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            best = max(best, len(heap))

        return best
```

## Complexity

- Time: `O(n log n)`
- Space: `O(n)`

## Historical Connection

This grows naturally out of:

- `Merge Intervals`
- `Video Stitching`

The extra idea is that now you are managing a dynamic set of overlapping resources, not just merging or covering ranges.
