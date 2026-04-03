# Shortest Word Distance II

- Difficulty: `MEDIUM`
- Frequency In CSV: `63.2`
- Acceptance Rate In CSV: `0.621334883686483`
- Source: [LeetCode](https://leetcode.com/problems/shortest-word-distance-ii)
- Topics: `Array, Hash Table, Two Pointers, String, Design`

## Framework Classification

- Input structure: static document plus repeated queries.
- Output asks for fast shortest-distance answers across many calls.
- Repeated operation: merge two sorted position lists.
- Remembered state: per-word sorted occurrence indices.

## Pattern Choice

- Primary: Preprocess positions, then answer with two pointers.
- Secondary: Hash map lookup gets you to the relevant lists quickly.

## Why This Matches The Framework

The framework says store information when the same work repeats. Since the words array is fixed, preprocessing pays for itself.

## Invariant

The two pointers always reference the smallest unseen candidate positions in each list.

## Skeleton Plan

1. Build a map from word to sorted occurrence indices.
2. For each query, walk the two index lists with two pointers.
3. Update the minimum distance and advance the smaller index.

## Complexity

Preprocessing `O(n)`, each query `O(a + b)`.

## Common Pitfalls

- Do not rescan the entire document per query.
- Two sorted lists are why the merge-style walk is linear.
- This is a design problem, so repeated-query efficiency matters.

## Python Solution

```python
from collections import defaultdict


class WordDistance:
    def __init__(self, wordsDict: list[str]):
        self.positions = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.positions[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        a = self.positions[word1]
        b = self.positions[word2]
        i = 0
        j = 0
        best = float("inf")

        while i < len(a) and j < len(b):
            best = min(best, abs(a[i] - b[j]))
            if a[i] < b[j]:
                i += 1
            else:
                j += 1

        return best
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
