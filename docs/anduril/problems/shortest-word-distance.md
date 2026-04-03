# Shortest Word Distance

- Difficulty: `EASY`
- Frequency In CSV: `85.6`
- Acceptance Rate In CSV: `0.6594949449257005`
- Source: [LeetCode](https://leetcode.com/problems/shortest-word-distance)
- Topics: `Array, String`

## Framework Classification

- Input structure: linear array of words.
- Output asks for a minimum distance.
- Repeated operation: update the best answer whenever one target reappears.
- Remembered state: last seen positions of relevant words.

## Pattern Choice

- Primary: One-pass scan with last-seen indices.
- Secondary: No heavy data structure is needed.

## Why This Matches The Framework

The framework says to try the smallest viable state-tracking scan first. This is a repeated nearest-neighbor update problem.

## Invariant

The stored indices are always the best prior candidates for forming the next shortest distance.

## Skeleton Plan

1. Track the last index of each target word.
2. Whenever either target appears, update its last-seen index.
3. If both targets have been seen, update the minimum distance.

## Complexity

Time `O(n)`, space `O(1)`.

## Common Pitfalls

- Update the answer after each relevant word.
- Do not fall back to nested loops.
- Variants where the two target words can be the same need special handling.

## Python Solution

```python
class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        i1 = -1
        i2 = -1
        best = len(wordsDict)

        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i
            if word == word2:
                i2 = i

            if i1 != -1 and i2 != -1:
                best = min(best, abs(i1 - i2))

        return best
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
