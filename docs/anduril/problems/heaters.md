# Heaters

- Difficulty: `MEDIUM`
- Frequency In CSV: `82.5`
- Acceptance Rate In CSV: `0.39952991914941977`
- Source: [LeetCode](https://leetcode.com/problems/heaters)
- Topics: `Array, Two Pointers, Binary Search, Sorting`

## Framework Classification

- Input structure: two sets of positions on a number line.
- Output asks for a global minimum radius that covers every house.
- Repeated operation: find the nearest heater to each house.
- Useful structure: sorting turns this into local neighbor lookup.

## Pattern Choice

- Primary: Sort heaters and binary search nearest heater for each house.
- Secondary: Two pointers is another good sorted-order solution.

## Why This Matches The Framework

The framework says sorted order plus local nearest-neighbor queries often means binary search or two pointers.

## Invariant

For each house, you compute its exact distance to the closest heater, and the answer is the maximum of those distances.

## Skeleton Plan

1. Sort heater positions.
2. For each house, binary search the insertion point among heaters.
3. Compare the left and right heater candidate distances.
4. Track the maximum nearest-heater distance.

## Complexity

Time `O(h log k)` if you binary search each house.

## Common Pitfalls

- Boundary cases occur when only a left or right heater exists.
- The final answer is the max over houses, not a min.
- Sorting is the simplifying step.

## Python Solution

```python
from bisect import bisect_left


class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        heaters.sort()
        radius = 0

        for house in houses:
            i = bisect_left(heaters, house)
            left_dist = house - heaters[i - 1] if i > 0 else float("inf")
            right_dist = heaters[i] - house if i < len(heaters) else float("inf")
            radius = max(radius, min(left_dist, right_dist))

        return radius
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
