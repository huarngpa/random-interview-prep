# Minesweeper

- Difficulty: `MEDIUM`
- Frequency In CSV: `53.9`
- Acceptance Rate In CSV: `0.681241547837878`
- Source: [LeetCode](https://leetcode.com/problems/minesweeper)
- Topics: `Array, Depth-First Search, Breadth-First Search, Matrix`

## Framework Classification

- Input structure: grid with recursive reveal rules.
- Output asks for updated board state.
- Repeated operation: reveal neighbors when a cell has no adjacent mines.
- Remembered state: which cells have already been processed.

## Pattern Choice

- Primary: DFS or BFS reveal simulation.
- Secondary: DFS often reads more naturally.

## Why This Matches The Framework

The framework says grid traversal with local rules. This is state expansion, not path optimization.

## Invariant

Once a cell is revealed and its adjacent-mine count is determined, its final state is fixed.

## Skeleton Plan

1. Handle a clicked mine immediately.
2. Otherwise count adjacent mines around the current cell.
3. If the count is positive, write the digit.
4. If the count is zero, mark blank and recursively reveal neighbors.

## Complexity

Time proportional to the number of revealed cells.

## Common Pitfalls

- This problem uses 8-direction adjacency.
- Do not revisit already revealed cells.
- A mine click ends the process immediately.

## Python Solution

```python
class Solution:
    def updateBoard(self, board: list[list[str]], click: list[int]) -> list[list[str]]:
        rows, cols = len(board), len(board[0])
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1),
        ]

        def count_mines(r: int, c: int) -> int:
            total = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "M":
                    total += 1
            return total

        def dfs(r: int, c: int) -> None:
            if not (0 <= r < rows and 0 <= c < cols):
                return
            if board[r][c] != "E":
                return

            mines = count_mines(r, c)
            if mines > 0:
                board[r][c] = str(mines)
                return

            board[r][c] = "B"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        r, c = click
        if board[r][c] == "M":
            board[r][c] = "X"
        else:
            dfs(r, c)

        return board
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
