# Game of Life

- Difficulty: `MEDIUM`
- Frequency In CSV: `53.9`
- Acceptance Rate In CSV: `0.7141499668480139`
- Source: [LeetCode](https://leetcode.com/problems/game-of-life)
- Topics: `Array, Matrix, Simulation`

## Framework Classification

- Input structure: grid updated simultaneously from local rules.
- Output asks for the next state in place.
- Repeated operation: count neighbors while preserving original state visibility.
- Key constraint: simultaneous updates.

## Pattern Choice

- Primary: Simulation with temporary state encoding.
- Secondary: Copying the board is conceptually simpler but costs extra space.

## Why This Matches The Framework

The framework says simulation when local rules dominate. The interesting trick is preserving enough old-state information while writing new-state information in place.

## Invariant

During the first pass, every cell still reveals its original alive/dead state even if it carries a transitional marker.

## Skeleton Plan

1. For each cell, count live neighbors according to original state.
2. Encode transitions with temporary markers.
3. In a second pass, normalize every cell to its final 0/1 state.

## Complexity

Time `O(m * n)`, extra space `O(1)` with transitional markers.

## Common Pitfalls

- Neighbor checks are 8-directional.
- Simultaneous update semantics are the whole point of the problem.
- Count neighbors by original state, not final state.

## Python Solution

```python
class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1),
        ]

        def live_neighbors(r: int, c: int) -> int:
            total = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in (1, -1):
                    total += 1
            return total

        for r in range(rows):
            for c in range(cols):
                neighbors = live_neighbors(r, c)
                if board[r][c] == 1 and (neighbors < 2 or neighbors > 3):
                    board[r][c] = -1
                elif board[r][c] == 0 and neighbors == 3:
                    board[r][c] = 2

        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
