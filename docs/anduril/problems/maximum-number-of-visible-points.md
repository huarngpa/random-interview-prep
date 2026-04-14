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

## Deeper Intuition

This problem looks geometric, but the hard part is not really geometry.

The real move is:

- turn every point into an angle around you
- sort those angles
- find the biggest group that fits inside an angle-sized window

Once you do that, this becomes a sliding-window problem on a sorted array.

The annoying part is that angles wrap around.

For example, suppose your field of view is `30` degrees and the interesting points are near:

- `350` degrees
- `355` degrees
- `5` degrees
- `10` degrees

Those points are actually close together on a circle, but in a normal sorted array they look split apart across the `0/360` boundary.

That is why we duplicate the angle list with `+ 2 * pi`.

If the original sorted angles are:

- `5`
- `10`
- `350`
- `355`

then after converting to radians and extending, the second copy gives us a fake "continued circle" so that a wrapped arc can be seen as one normal contiguous window.

That is the entire trick.

## What The Doubled Array Is Doing

Suppose the sorted angle list is:

- `a1`
- `a2`
- `a3`

Then we build:

- `a1`
- `a2`
- `a3`
- `a1 + 2*pi`
- `a2 + 2*pi`
- `a3 + 2*pi`

This gives us a `720` degree search space instead of a `360` degree circle.

We are not changing the geometry.

We are just making wraparound windows behave like ordinary subarrays.

That lets two pointers work cleanly.

## Complexity

Time `O(n log n)` for sorting, space `O(n)`.

## Common Pitfalls

- Do not forget points at the same location as the observer.
- Be consistent about degrees versus radians.
- The doubled angle array is what handles circular wraparound cleanly.

## Sliding Window Walkthrough

This is the core of the solution:

```python
field_of_view = math.radians(angle)
search_space = angles + [a + 2 * math.pi for a in angles]

max_points_visible = 0
start_of_view = 0

for end_of_view in range(len(search_space)):
    current_angle = search_space[end_of_view]

    while current_angle - search_space[start_of_view] > field_of_view + 1e-12:
        start_of_view += 1

    points_in_this_window = end_of_view - start_of_view + 1
    max_points_visible = max(max_points_visible, points_in_this_window)
```

Here is what each part means.

### 1. Convert The User's Angle To Radians

```python
field_of_view = math.radians(angle)
```

`atan2` gives us angles in radians, so the visibility angle also needs to be in radians.

If the user says `90`, we convert that to the radian value for a quarter turn.

### 2. Build A Search Space That Can Cross The Wraparound

```python
search_space = angles + [a + 2 * math.pi for a in angles]
```

The original `angles` array lives on a circle.

The doubled `search_space` array lets us pretend that circle has been unrolled into a straight line long enough to include any wrapped interval.

This means a window like:

- from `350` degrees
- to `10` degrees

can now be seen as one ordinary interval in the extended array.

### 3. `start_of_view` And `end_of_view` Define The Current Visible Arc

```python
max_points_visible = 0
start_of_view = 0
```

At any moment:

- `start_of_view` is the left edge of the current arc
- `end_of_view` is the right edge of the current arc

Everything between them is our current guess for "points visible at once."

### 4. Advance The Right Edge One Point At A Time

```python
for end_of_view in range(len(search_space)):
    current_angle = search_space[end_of_view]
```

We try every possible right boundary.

So the algorithm is really asking:

- if this angle is the far-right point in my visible arc
- how far left can I go while still staying inside the allowed field of view?

### 5. Shrink From The Left Until The Window Is Valid Again

```python
while current_angle - search_space[start_of_view] > field_of_view + 1e-12:
    start_of_view += 1
```

This is the heart of the solution.

`current_angle - search_space[start_of_view]` is the width of the current arc.

If that width is too large, the window is invalid, so we move the left edge forward until the arc fits again.

The tiny `1e-12` is just protection against floating-point noise. Without it, values that should be equal can sometimes compare slightly wrong.

### 6. Measure The Valid Window

```python
points_in_this_window = end_of_view - start_of_view + 1
max_points_visible = max(max_points_visible, points_in_this_window)
```

Once the window is valid again, the number of visible points is just the number of entries between the two pointers.

We keep the biggest one we ever see.

### 7. Add Back The Points At Your Exact Location

Points exactly on the observer's location are always visible, no matter which direction you face.

That is why the final answer is:

```python
return max_points_visible + same_location
```

Those points are not part of the angle math at all. They are free points that always count.

## Python Solution

```python
import math
from typing import List


class Solution:
    def visiblePoints(
        self,
        points: List[List[int]],
        angle: int,
        location: List[int],
    ) -> int:
        x0, y0 = location[0], location[1]
        same_location = 0
        angles = []

        for point in points:
            x, y = point[0], point[1]
            dx, dy = x - x0, y - y0
            if dx == 0 and dy == 0:
                same_location += 1
            else:
                angles.append(math.atan2(dy, dx))

        angles.sort()

        fov = math.radians(angle)
        extended = angles + [a + 2 * math.pi for a in angles]
        best = 0
        left = 0

        for right, a in enumerate(extended):
            while a - extended[left] > fov:
                left += 1
            best = max(best, right - left + 1)

        return best + same_location
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
