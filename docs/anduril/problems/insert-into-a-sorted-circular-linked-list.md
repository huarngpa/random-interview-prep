# Insert into a Sorted Circular Linked List

- Difficulty: `MEDIUM`
- Frequency In CSV: `53.9`
- Acceptance Rate In CSV: `0.38124104725048336`
- Source: [LeetCode](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list)
- Topics: `Linked List`

## Framework Classification

- Input structure: sorted circular linked list.
- Output asks for correct insertion while preserving circular order.
- Repeated operation: inspect each directed edge as a candidate insertion location.
- Remembered state: current node and its next node.

## Pattern Choice

- Primary: Single traversal with careful case analysis.
- Secondary: This is more pointer reasoning than a named algorithm pattern.

## Why This Matches The Framework

The framework says start from the data structure constraints. The key distinction is normal sorted edges versus the wraparound pivot edge.

## Invariant

At every step, you are evaluating whether the edge `curr -> curr.next` is the correct insertion boundary.

## Skeleton Plan

1. Handle the empty-list case by creating a self-loop node.
2. Traverse the cycle looking for an in-range spot or the wraparound pivot.
3. If no special spot appears after one full loop, insert anywhere and preserve the cycle.

## Complexity

Time `O(n)`, space `O(1)`.

## Common Pitfalls

- The pivot edge is where `curr.val > curr.next.val`.
- All-equal lists still need a valid insertion after a full loop.
- Be careful to stop after one cycle.

## Python Solution

```python
# class Node:
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        if not head:
            new_node.next = new_node
            return new_node

        curr = head
        while True:
            nxt = curr.next

            if curr.val <= insertVal <= nxt.val:
                break

            if curr.val > nxt.val and (insertVal >= curr.val or insertVal <= nxt.val):
                break

            curr = nxt
            if curr == head:
                break

        new_node.next = curr.next
        curr.next = new_node
        return head
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
