# Spiral Matrix

- LeetCode: [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
- Why It Is Likely: this is a classic matrix traversal Medium and fits the fast first-problem slot in a two-question screen.

## Why Anduril Asks This

This problem looks simple, but it tests something Anduril likely cares about:

- can you stay organized while walking structured state?
- can you manage boundaries carefully without getting lost?
- can you implement a deterministic process cleanly?

That maps to internal factory software more than it first appears:

- traversing structured operational data
- walking ordered layouts or work instructions
- keeping tight control over state transitions and boundaries

It is less about cleverness and more about disciplined implementation.

## Framework Classification

- Input structure: rectangular matrix
- Output asks for an ordered traversal
- Repeated operation: consume one boundary at a time
- Remembered state: top, bottom, left, right boundaries

## Pattern Choice

- Primary: boundary simulation
- Secondary: direction arrays also work, but four shrinking boundaries are easier to explain

## Principle To Internalize

Treat the remaining unvisited region as a shrinking rectangle.

Each loop:

1. consume the top row
2. consume the right column
3. consume the bottom row if still valid
4. consume the left column if still valid

Then shrink the rectangle.

## Solving Walkthrough

1. Initialize `top`, `bottom`, `left`, and `right`.
2. While the rectangle is still valid:
3. Walk left to right across the top row.
4. Walk top to bottom down the right column.
5. If rows remain, walk right to left across the bottom row.
6. If columns remain, walk bottom to top up the left column.
7. Repeat until the bounds cross.

## Python Solution

```python
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1

            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result
```

## Complexity

- Time: `O(rows * cols)`
- Space: `O(1)` extra space besides the output

## Interview Notes

- Say that this is simulation with shrinking boundaries.
- Guard the bottom-row and left-column passes carefully.
- This is a great problem to narrate with a `3 x 4` example while coding.
