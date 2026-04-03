# Rotting Oranges

- Difficulty: `MEDIUM`
- Frequency In CSV: `53.9`
- Acceptance Rate In CSV: `0.5661842002497466`
- Source: [LeetCode](https://leetcode.com/problems/rotting-oranges)
- Topics: `Array, Breadth-First Search, Matrix`

## Framework Classification

- Input structure: grid with simultaneous spread over time.
- Output asks for minimum time until the process completes.
- Repeated operation: expand one wave of infection/rot per minute.
- Remembered state: queue of active sources and remaining fresh count.

## Pattern Choice

- Primary: Multi-source BFS.
- Secondary: Repeated rescans are slower and conceptually weaker.

## Why This Matches The Framework

The framework says unweighted minimum steps means BFS. Multiple starting sources simply means the initial queue has many nodes.

## Invariant

The first time a cell is reached in BFS is the earliest time it can change state.

## Skeleton Plan

1. Queue all starting rotten sources and count fresh cells.
2. Process the queue level by level.
3. When a fresh neighbor changes, decrement the fresh count and enqueue it.
4. Return elapsed levels if everything is reached, otherwise `-1`.

## Complexity

Time `O(rows * cols)`, space `O(rows * cols)`.

## Common Pitfalls

- Return `0` immediately if nothing needs to change.
- Track fresh count so impossible cases are easy to detect.
- This is BFS because time moves in discrete waves.

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
        for_dr = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            r, c, minutes = queue.popleft()
            for dr, dc in for_dr:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, minutes + 1))

        return minutes if fresh == 0 else -1
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
