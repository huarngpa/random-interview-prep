# Number of Distinct Islands

- Difficulty: `MEDIUM`
- Frequency In CSV: `53.9`
- Acceptance Rate In CSV: `0.6225531873624047`
- Source: [LeetCode](https://leetcode.com/problems/number-of-distinct-islands)
- Topics: `Hash Table, Depth-First Search, Breadth-First Search, Union Find, Hash Function`

## Framework Classification

- Input structure: grid of connected components.
- Output asks for the number of unique component shapes.
- Repeated operation: traverse one component and build a canonical signature.
- Remembered state: visited cells and a set of shape encodings.

## Pattern Choice

- Primary: DFS or BFS plus canonical shape signature.
- Secondary: Relative coordinates or traversal-path encoding both work.

## Why This Matches The Framework

The framework says this is Number of Islands plus a hashing layer. You still find components first, then hash only the structure needed for comparison.

## Invariant

Each island is traversed once and transformed into a translation-invariant signature before insertion into the set.

## Skeleton Plan

1. Find an unseen island and traverse it.
2. Record the island shape relative to its start or via a path signature.
3. Insert the signature into a set.
4. Return the size of the set.

## Complexity

Time `O(rows * cols)`, space `O(rows * cols)`.

## Common Pitfalls

- The signature must ignore absolute position.
- Path signatures need backtracking markers to avoid collisions.
- This asks for distinct shapes, not total islands.

## Python Solution

```python
class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        shapes = set()

        def dfs(r: int, c: int, base_r: int, base_c: int, shape: list[tuple[int, int]]) -> None:
            if not (0 <= r < rows and 0 <= c < cols):
                return
            if grid[r][c] != 1:
                return

            grid[r][c] = 0
            shape.append((r - base_r, c - base_c))

            dfs(r + 1, c, base_r, base_c, shape)
            dfs(r - 1, c, base_r, base_c, shape)
            dfs(r, c + 1, base_r, base_c, shape)
            dfs(r, c - 1, base_r, base_c, shape)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    shape = []
                    dfs(r, c, r, c, shape)
                    shapes.add(tuple(shape))

        return len(shapes)
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
