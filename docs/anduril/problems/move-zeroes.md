# Move Zeroes

- Difficulty: `EASY`
- Frequency In CSV: `53.9`
- Acceptance Rate In CSV: `0.6280404294781053`
- Source: [LeetCode](https://leetcode.com/problems/move-zeroes)
- Topics: `Array, Two Pointers`

## Framework Classification

- Input structure: array to be modified in place.
- Output asks for stable compaction of nonzero values.
- Repeated operation: write each kept value into the next open position.
- Remembered state: read pointer and write pointer.

## Pattern Choice

- Primary: Two pointers.
- Secondary: Overwrite-then-fill-zero is often simpler than repeated swaps.

## Why This Matches The Framework

The framework says use pointers when you can maintain a compact valid prefix while scanning once.

## Invariant

Everything before the write pointer is the correct nonzero prefix in original order.

## Skeleton Plan

1. Scan with a read pointer.
2. Whenever you see a nonzero, move or write it into the current write slot.
3. Advance the write pointer only on nonzeros.
4. Fill any remaining tail positions with zero.

## Complexity

Time `O(n)`, space `O(1)`.

## Common Pitfalls

- Preserve the relative order of nonzero values.
- The array must be modified in place.
- A clean overwrite approach is often easier to reason about than many swaps.

## Python Solution

```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        while write < len(nums):
            nums[write] = 0
            write += 1
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
