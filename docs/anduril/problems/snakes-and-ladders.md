# Snakes and Ladders

- Difficulty: `MEDIUM`
- Frequency In CSV: `53.9`
- Acceptance Rate In CSV: `0.47795353738879465`
- Source: [LeetCode](https://leetcode.com/problems/snakes-and-ladders)
- Topics: `Array, Breadth-First Search, Matrix`

## Framework Classification

- Input structure: board positions with deterministic transitions.
- Output asks for minimum number of moves.
- Repeated operation: expand all destinations reachable in one die roll.
- Remembered state: visited board positions.

## Pattern Choice

- Primary: BFS on an implicit graph.
- Secondary: A coordinate-conversion helper is often the hardest implementation detail.

## Why This Matches The Framework

The framework says unweighted minimum moves means BFS. Snakes and ladders are just redirected edges in that graph.

## Invariant

The first time a square is visited in BFS, it has been reached in the minimum number of moves.

## Skeleton Plan

1. Write a helper to convert square numbers into board coordinates.
2. Start BFS from square 1.
3. For each square, try die outcomes 1 through 6, apply any snake or ladder, and enqueue unseen destinations.
4. Return the BFS level when the last square is reached.

## Complexity

Time `O(n^2)`, space `O(n^2)`.

## Common Pitfalls

- Board rows alternate traversal direction.
- Apply a snake or ladder at most once per move.
- Visited tracking prevents cycles and duplicate work.

## Python Solution

```python
from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)

        def get_position(square: int) -> tuple[int, int]:
            quot, rem = divmod(square - 1, n)
            row = n - 1 - quot
            col = rem if quot % 2 == 0 else n - 1 - rem
            return row, col

        queue = deque([(1, 0)])
        seen = {1}

        while queue:
            square, steps = queue.popleft()
            if square == n * n:
                return steps

            for move in range(1, 7):
                nxt = square + move
                if nxt > n * n:
                    break

                r, c = get_position(nxt)
                if board[r][c] != -1:
                    nxt = board[r][c]

                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, steps + 1))

        return -1
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
