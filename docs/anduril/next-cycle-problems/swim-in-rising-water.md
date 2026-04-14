# Swim in Rising Water

- LeetCode: [778. Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)
- Why It Is Likely: this is a stronger next-step version of Anduril's grid family. It looks like a matrix problem, but the real structure is shortest path under a max-cost objective.

## Pattern Family

- graph shortest path
- heap / Dijkstra-style frontier search

## Framework Classification

- Input structure: grid of elevations
- Output asks for the minimum time required to reach the goal
- Repeated operation: expand the next best reachable state
- Hidden structure: each cell is a node, edges connect neighbors, path cost is the maximum elevation on the path

## Principle To Internalize

This is not ordinary BFS.

The path cost is not:

- number of steps

It is:

- the highest elevation you have had to tolerate so far

So the right state is:

- current cell
- best known maximum elevation along the path to reach it

That is Dijkstra territory.

## Solving Walkthrough

1. Use a min-heap keyed by the current path cost.
2. Start from `(0, 0)` with cost `grid[0][0]`.
3. Pop the cheapest state.
4. For each neighbor, the new path cost is `max(current_cost, neighbor_height)`.
5. The first time you pop the target, you have the optimum answer.

## Python Solution

```python
import heapq


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}

        while heap:
            cost, r, c = heapq.heappop(heap)
            if (r, c) == (n - 1, n - 1):
                return cost

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < n):
                    continue
                if (nr, nc) in seen:
                    continue
                seen.add((nr, nc))
                heapq.heappush(heap, (max(cost, grid[nr][nc]), nr, nc))

        return -1
```

## Complexity

- Time: `O(n^2 log n)`
- Space: `O(n^2)`

## Historical Connection

This fits the same world as:

- `Number of Islands`
- `Rotting Oranges`
- `Snakes and Ladders`

The upgrade is that you now need heap-based path selection rather than plain traversal.
