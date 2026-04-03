# Find the Duplicate Number

- Difficulty: `MEDIUM`
- Frequency In CSV: `53.9`
- Acceptance Rate In CSV: `0.6283574412311195`
- Source: [LeetCode](https://leetcode.com/problems/find-the-duplicate-number)
- Topics: `Array, Two Pointers, Binary Search, Bit Manipulation`

## Framework Classification

- Input structure: array values constrained to an index-like range.
- Output asks for the repeated value under strict memory constraints.
- Repeated operation: follow value-to-index transitions.
- Remembered state: slow and fast pointers over the implicit graph.

## Pattern Choice

- Primary: Floyd cycle detection on the implicit linked structure.
- Secondary: Binary search on value counts is another recognized solution.

## Why This Matches The Framework

The framework says to look for hidden graph structure when the prompt blocks simple sorting or hashing. Here the array induces a cycle whose entry is the duplicate number.

## Invariant

Slow and fast pointers meet inside the cycle, and the standard reset step finds the cycle entry.

## Skeleton Plan

1. Interpret each value as the next pointer.
2. Run slow and fast pointers until they meet.
3. Reset one pointer to the start and move both one step at a time.
4. Return the value where they meet again.

## Complexity

Time `O(n)`, space `O(1)`.

## Common Pitfalls

- This is a hidden-structure problem; the linked-list model is the key insight.
- Do not modify the input if following the strict constraints.
- The binary-search alternative searches the value space, not indices.

## Python Solution

```python
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
