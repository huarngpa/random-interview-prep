# Number of Islands

- Difficulty: `MEDIUM`
- Frequency In CSV: `100.0`
- Acceptance Rate In CSV: `0.6232005375415705`
- Source: [LeetCode](https://leetcode.com/problems/number-of-islands)
- Topics: `Array, Depth-First Search, Breadth-First Search, Union Find, Matrix`

## Framework Classification

- Input structure: a 2D grid that acts like a hidden graph.
- Output asks for the number of connected components.
- Repeated operation: explore neighboring land cells from a starting cell.
- Remembered state: visited cells or in-place marks.

## Pattern Choice

- Primary: DFS or BFS flood fill on a grid.
- Secondary: Union Find is a valid component-based alternative.

## Why This Matches The Framework

Our framework treats each land cell as a node and 4-direction adjacency as edges. The question is connected-component counting, not shortest path.

## Invariant

Once a land cell is visited, it already belongs to a counted island and must never start another island count.

## Skeleton Plan

1. Scan the full grid.
2. When you hit unseen land, increment the answer.
3. Run DFS or BFS to mark the entire component.
4. Continue the scan until every cell is classified.

## Complexity

Time `O(rows * cols)`, space up to `O(rows * cols)` depending on visited storage and recursion/queue usage.

## Common Pitfalls

- Only 4-direction adjacency counts unless the prompt says otherwise.
- Handle an empty grid safely.
- If you mutate the grid, note that the input cannot be reused afterward.

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

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
