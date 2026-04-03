# Search in Rotated Sorted Array

- Difficulty: `MEDIUM`
- Frequency In CSV: `53.9`
- Acceptance Rate In CSV: `0.4283722145334321`
- Source: [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array)
- Topics: `Array, Binary Search`

## Framework Classification

- Input structure: rotated sorted array.
- Output asks for a target position.
- Repeated operation: decide which half is normally sorted and whether the target lies there.
- Useful structure: at least one half around any midpoint remains sorted.

## Pattern Choice

- Primary: Modified binary search.
- Secondary: You can find the pivot first, but it is not necessary.

## Why This Matches The Framework

The framework still says binary search because enough order remains to eliminate half the space each step.

## Invariant

After each comparison, the chosen half is guaranteed to still contain the target if it exists.

## Skeleton Plan

1. Compute `mid`.
2. Determine whether the left or right half is normally sorted.
3. Check if the target lies inside that sorted half.
4. Discard the other half and continue.

## Complexity

Time `O(log n)`, space `O(1)`.

## Common Pitfalls

- Be precise with inclusive boundaries.
- This common version assumes distinct values.
- Check for direct midpoint match before sorted-half branching.

## Python Solution

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
