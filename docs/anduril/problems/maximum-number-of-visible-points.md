# Maximum Number of Visible Points

- Difficulty: `HARD`
- Frequency In CSV: `92.9`
- Acceptance Rate In CSV: `0.3767605072174815`
- Source: [LeetCode](https://leetcode.com/problems/maximum-number-of-visible-points)
- Topics: `Array, Math, Geometry, Sliding Window, Sorting`

## Framework Classification

- Input structure: 2D points plus an angular visibility constraint.
- Output asks for the largest valid contiguous angular window.
- Repeated operation: maintain how many sorted angles fit inside the allowed field of view.
- Remembered state: sorted angle list and sliding window boundaries.

## Pattern Choice

- Primary: Convert points to polar angles, sort them, duplicate by `+360`, then use sliding window.
- Secondary: The geometry step is just preprocessing with `atan2`.

## Why This Matches The Framework

The framework says to impose order first. Once geometry is reduced to sorted angles, the core becomes a contiguous-window problem.

## Invariant

The current window always represents a valid arc whose angular width is at most the allowed angle.

## Skeleton Plan

1. Count points exactly at the observer separately.
2. Convert all other points to angles.
3. Sort the angles and append a shifted copy to handle wraparound.
4. Use two pointers to keep the largest valid angular window.

## Complexity

Time `O(n log n)` for sorting, space `O(n)`.

## Common Pitfalls

- Do not forget points at the same location as the observer.
- Be consistent about degrees versus radians.
- The doubled angle array is what handles circular wraparound cleanly.

## Python Solution

```python
import math


class Solution:
    def visiblePoints(
        self,
        points: list[list[int]],
        angle: int,
        location: list[int],
    ) -> int:
        same_location = 0
        angles = []
        x0, y0 = location

        for x, y in points:
            dx = x - x0
            dy = y - y0
            if dx == 0 and dy == 0:
                same_location += 1
            else:
                angles.append(math.atan2(dy, dx))

        angles.sort()
        extended = angles + [a + 2 * math.pi for a in angles]
        field = math.radians(angle)

        best = 0
        left = 0
        for right, current in enumerate(extended):
            while current - extended[left] > field + 1e-12:
                left += 1
            best = max(best, right - left + 1)

        return best + same_location
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
