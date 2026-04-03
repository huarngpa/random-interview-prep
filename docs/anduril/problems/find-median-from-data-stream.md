# Find Median from Data Stream

- Difficulty: `HARD`
- Frequency In CSV: `79.0`
- Acceptance Rate In CSV: `0.5327803189283605`
- Source: [LeetCode](https://leetcode.com/problems/find-median-from-data-stream)
- Topics: `Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream`

## Framework Classification

- Input structure: streaming inserts plus repeated median queries.
- Output asks for a dynamic middle value.
- Repeated operation: maintain balanced lower and upper halves.
- Remembered state: two heaps.

## Pattern Choice

- Primary: Two heaps: max-heap for lower half and min-heap for upper half.
- Secondary: Balanced trees work too but are less Python-friendly.

## Why This Matches The Framework

The framework says use heaps when you repeatedly need dynamic boundary values. Median specifically needs fast access to both middle boundaries.

## Invariant

Heap sizes differ by at most one, and every value in the lower heap is less than or equal to every value in the upper heap.

## Skeleton Plan

1. Insert into one heap.
2. Fix ordering between heaps if needed.
3. Rebalance sizes so they differ by at most one.
4. Answer median queries from one heap top or the average of both heap tops.

## Complexity

Insert `O(log n)`, median query `O(1)`.

## Common Pitfalls

- Python only provides a min-heap, so use negatives for the max-heap.
- Keep both size and ordering invariants.
- Rebalancing is part of every insert.

## Python Solution

```python
import heapq


class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
