# Number of Islands

- LeetCode: [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
- Why It Is Likely: this is one of the most common Anduril-tagged problems and a canonical grid/graph Medium.

## Why Anduril Asks This

This is not really about islands.

It is about whether you can look at a 2D operational layout and immediately recognize:

- hidden graph structure
- connected components
- local traversal rules
- how to avoid double counting

That maps cleanly to Forge and ArsenalOS thinking:

- factory floor zones
- sensor regions
- disconnected work cells
- layout-based reasoning over manufacturing state

They are testing whether you can turn a physical-looking problem into a software model quickly.

## Framework Classification

- Input structure: grid with land and water
- Output asks for a count of connected components
- Repeated operation: flood fill one component
- Remembered state: visited cells or in-place marking

## Pattern Choice

- Primary: DFS or BFS on a grid
- Secondary: Union find also works, but DFS is the fastest interview answer

## Principle To Internalize

The moment you see:

- 2D grid
- adjacency
- count the groups

you should think:

- this is connected components in a hidden graph

That means:

- scan the grid
- every time you discover fresh land, you found a new island
- consume the whole island immediately

## Solving Walkthrough

1. Scan every cell.
2. If the cell is water, ignore it.
3. If the cell is land, increment the island count.
4. Run DFS to mark the entire connected component as visited.
5. Continue scanning until the whole grid is classified.

## Python Solution

```python
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int) -> None:
            if not (0 <= r < rows and 0 <= c < cols):
                return
            if grid[r][c] != "1":
                return

            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands
```

## Complexity

- Time: `O(rows * cols)`
- Space: `O(rows * cols)` in the worst case from recursion depth

## Interview Notes

- Say "hidden graph" early.
- Be explicit that this is not shortest path.
- Mention that mutating the grid avoids an extra visited set.
