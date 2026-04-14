# Game of Life

- LeetCode: [289. Game of Life](https://leetcode.com/problems/game-of-life/)
- Why It Is Likely: this is a detail-heavy matrix simulation problem that fits Anduril’s operational flavor very well.

## Why Anduril Asks This

This problem tests whether you can reason about:

- a stateful system
- local rules
- synchronous updates
- careful implementation under mutation constraints

That is exactly the kind of thinking you need in production software:

- a board today represents the current plant state
- the next board represents the next system state
- all updates must be computed from the old state, not partially updated state

This is less about algorithms-as-tricks and more about being careful with transition semantics.

## Framework Classification

- Input structure: matrix with local update rules
- Output asks for next system state
- Repeated operation: inspect each cell and count live neighbors
- Remembered state: current board plus temporary transition markers

## Pattern Choice

- Primary: simulation with encoded in-place state transitions
- Secondary: using a copy of the board is easier conceptually but uses extra space

## Principle To Internalize

The hard part is not counting neighbors.

The hard part is:

- every cell's next state depends on the original board
- but you are asked to update in place

So the trick is to encode transitions:

- `1 -> 0` as `-1`
- `0 -> 1` as `2`

That way:

- the old state is still recoverable while scanning
- the final cleanup pass converts markers to final values

## Solving Walkthrough

1. For every cell, count live neighbors using the original-state interpretation.
2. If a live cell should die, mark it `-1`.
3. If a dead cell should become live, mark it `2`.
4. After the full scan, do a second pass.
5. Convert positive values to `1` and non-positive values to `0`.

## Python Solution

```python
class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = (
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1),
        )

        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                        live_neighbors += 1

                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1
                elif board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2

        for r in range(rows):
            for c in range(cols):
                board[r][c] = 1 if board[r][c] > 0 else 0
```

## Complexity

- Time: `O(rows * cols)`
- Space: `O(1)` extra space

## Interview Notes

- Say out loud that updates must be simultaneous.
- Explain why `abs(board[nr][nc]) == 1` means "originally alive."
- If short on time, you can mention that a copied-board version is simpler, then choose the in-place version if asked.
