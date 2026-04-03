# Making A Large Island

- Difficulty: `HARD`
- Frequency In CSV: `69.7`
- Acceptance Rate In CSV: `0.5489029735459547`
- Source: [LeetCode](https://leetcode.com/problems/making-a-large-island)
- Topics: `Array, Depth-First Search, Breadth-First Search, Union Find, Matrix`

## Framework Classification

- Input structure: grid components plus one allowed mutation.
- Output asks for the best component size after one flip.
- Repeated operation: combine neighboring component sizes around a water cell.
- Remembered state: component ids and component sizes.

## Pattern Choice

- Primary: Label islands first, then evaluate each zero cell by neighboring ids.
- Secondary: Union Find is a valid alternative.

## Why This Matches The Framework

The framework says solve the stable structure first, then apply the local optimization. Pre-labeling turns each candidate flip into a constant-neighborhood calculation.

## Invariant

Every land cell belongs to exactly one known component with a known area.

## Skeleton Plan

1. First pass: label each island and record its size.
2. Second pass: for every zero, gather unique neighboring component ids and sum their sizes plus one.
3. Track the maximum, including the all-land edge case.

## Complexity

Time `O(n^2)`, space `O(n^2)` in the worst case.

## Common Pitfalls

- Do not double-count the same neighboring island id.
- All-land grids should return the total cell count.
- Trying every flip from scratch is too expensive.

## Python Solution

```python
class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        island_size = {0: 0}
        island_id = 2

        def dfs(r: int, c: int, idx: int) -> int:
            if not (0 <= r < n and 0 <= c < n):
                return 0
            if grid[r][c] != 1:
                return 0

            grid[r][c] = idx
            size = 1
            size += dfs(r + 1, c, idx)
            size += dfs(r - 1, c, idx)
            size += dfs(r, c + 1, idx)
            size += dfs(r, c - 1, idx)
            return size

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_size[island_id] = dfs(r, c, island_id)
                    island_id += 1

        best = max(island_size.values(), default=0)

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    neighbors = {
                        grid[nr][nc]
                        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
                        if 0 <= nr < n and 0 <= nc < n
                    }
                    best = max(best, 1 + sum(island_size[idx] for idx in neighbors))

        return best
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
