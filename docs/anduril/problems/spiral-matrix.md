# Spiral Matrix

- Difficulty: `MEDIUM`
- Frequency In CSV: `53.9`
- Acceptance Rate In CSV: `0.5393974123278643`
- Source: [LeetCode](https://leetcode.com/problems/spiral-matrix)
- Topics: `Array, Matrix, Simulation`

## Framework Classification

- Input structure: matrix traversal.
- Output asks for an ordered simulation result.
- Repeated operation: walk one boundary, then shrink the remaining rectangle.
- Remembered state: top, bottom, left, and right boundaries.

## Pattern Choice

- Primary: Boundary simulation.
- Secondary: Visited-grid simulation is possible but less elegant.

## Why This Matches The Framework

The framework says use simulation when the problem is mostly about careful state evolution rather than deeper optimization.

## Invariant

The unvisited cells are always exactly the rectangle defined by the current boundaries.

## Skeleton Plan

1. Initialize four boundaries.
2. Traverse top row, right column, bottom row, and left column in order.
3. Shrink the corresponding boundary after each pass.
4. Guard each traversal with boundary checks.

## Complexity

Time `O(m * n)`, extra space `O(1)` beyond output.

## Common Pitfalls

- Boundary-crossing checks prevent duplicates on thin leftovers.
- This is mostly bookkeeping, so keep the loop structure clean.
- Single-row and single-column cases are where bugs usually hide.

## Python Solution

```python
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        answer = []

        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                answer.append(matrix[top][c])
            top += 1

            for r in range(top, bottom + 1):
                answer.append(matrix[r][right])
            right -= 1

            if top <= bottom:
                for c in range(right, left - 1, -1):
                    answer.append(matrix[bottom][c])
                bottom -= 1

            if left <= right:
                for r in range(bottom, top - 1, -1):
                    answer.append(matrix[r][left])
                left += 1

        return answer
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
