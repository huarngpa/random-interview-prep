# Merge k Sorted Lists

- Difficulty: `HARD`
- Frequency In CSV: `63.2`
- Acceptance Rate In CSV: `0.5677419253083275`
- Source: [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists)
- Topics: `Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort`

## Framework Classification

- Input structure: `k` sorted streams/lists.
- Output asks for one globally sorted stream.
- Repeated operation: choose the smallest current head.
- Remembered state: one candidate from each active list.

## Pattern Choice

- Primary: Min-heap over current heads.
- Secondary: Divide-and-conquer pairwise merging is another strong option.

## Why This Matches The Framework

The framework says heap when you repeatedly need the global minimum from several evolving sources.

## Invariant

The heap contains exactly the next candidate node from each list that still has elements remaining.

## Skeleton Plan

1. Push every non-null list head into a min-heap.
2. Pop the smallest node, append it to the output, and push its successor.
3. Repeat until the heap is empty.

## Complexity

Time `O(N log k)`, space `O(k)`.

## Common Pitfalls

- Python heap entries need a tiebreaker when node values tie.
- Pointer management is the tricky part in linked-list implementations.
- Divide-and-conquer gives the same asymptotic time if you prefer that style.

## Python Solution

```python
import heapq
from itertools import count
from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        ticket = count()

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, next(ticket), node))

        dummy = ListNode(0)
        tail = dummy

        while heap:
            _, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, next(ticket), node.next))

        return dummy.next
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
