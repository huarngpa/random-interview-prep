# Rotting Oranges

- LeetCode: [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
- Why It Is Likely: this is one of the cleanest multi-source BFS problems and feels very Anduril because it models state spread over time.

## Why Anduril Asks This

This one maps unusually well to factory and operations software.

You have:

- a grid
- multiple starting sources
- state that spreads over time
- a need to know when the whole process completes, or whether it is impossible

That is basically the same shape as:

- fault propagation
- machine state rollout
- staged production readiness
- status contamination or dependency spread across a layout

So this is a very plausible "operations thinking" problem for ArsenalOS.

## Framework Classification

- Input structure: grid with many starting sources
- Output asks for minimum time to reach all reachable targets
- Repeated operation: spread one layer per minute
- Remembered state: queue plus count of remaining fresh cells

## Pattern Choice

- Primary: multi-source BFS
- Secondary: repeated rescans are possible, but they are slower and conceptually weaker

## Principle To Internalize

This is just BFS with more than one start node.

The first important recognition is:

- unweighted shortest time to spread -> BFS

The second is:

- if several cells start active at time `0`, they all go in the queue immediately

## Solving Walkthrough

1. Scan the grid once.
2. Put every rotten orange into the queue with time `0`.
3. Count the number of fresh oranges.
4. Run BFS outward.
5. Whenever a fresh orange becomes rotten, decrement the fresh count and enqueue it with time `+1`.
6. If fresh reaches `0`, return the last time seen.
7. Otherwise return `-1`.

## Python Solution

```python
from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            r, c, minutes = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, minutes + 1))

        return minutes if fresh == 0 else -1
```

## Complexity

- Time: `O(rows * cols)`
- Space: `O(rows * cols)`

## Interview Notes

- Say "multi-source BFS" as soon as you see many initial rotten cells.
- Mention that BFS layer order gives earliest time automatically.
- Tracking `fresh` makes the impossible case easy.
