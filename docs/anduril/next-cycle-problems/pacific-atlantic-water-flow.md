# Pacific Atlantic Water Flow

- LeetCode: [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- Why It Is Likely: this feels like the next-step version of the historical grid/graph family. It is still a matrix traversal problem, but the real unlock is reversing the direction and using multi-source search.

## Pattern Family

- graph traversal on a grid
- reverse reachability
- multi-source DFS or BFS

## Framework Classification

- Input structure: height grid with directional flow constraints
- Output asks for cells satisfying two reachability conditions
- Repeated operation: explore where water could have come from
- Hidden structure: each cell is a node and valid reverse-flow moves are edges

## Principle To Internalize

Do not search outward from every cell.

Search inward from each ocean.

The hard-looking part of this problem disappears once you realize:

- "can water flow from this cell to the ocean?" is equivalent to
- "can the ocean reach this cell if I reverse the flow rule?"

That turns many searches into two multi-source traversals.

## Solving Walkthrough

1. Treat each ocean edge as a starting frontier.
2. From each frontier, move only to neighbors with height greater than or equal to the current cell.
3. Mark all cells reachable from the Pacific.
4. Mark all cells reachable from the Atlantic.
5. Intersect the two reachable sets.

## Python Solution

```python
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r: int, c: int, seen: set[tuple[int, int]]) -> None:
            seen.add((r, c))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                if (nr, nc) in seen:
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                dfs(nr, nc, seen)

        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)

        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)

        return [[r, c] for r in range(rows) for c in range(cols) if (r, c) in pacific and (r, c) in atlantic]
```

## Complexity

- Time: `O(rows * cols)`
- Space: `O(rows * cols)`

## Historical Connection

This is the same family as:

- `Number of Islands`
- `Rotting Oranges`
- `Making A Large Island`

The new trick is not traversal itself. It is recognizing that reversing the flow makes the traversal simple.
