# Merge Intervals

- Difficulty: `MEDIUM`
- Frequency In CSV: `69.7`
- Acceptance Rate In CSV: `0.49395255430023527`
- Source: [LeetCode](https://leetcode.com/problems/merge-intervals)
- Topics: `Array, Sorting`

## Framework Classification

- Input structure: intervals.
- Output asks for overlapping intervals collapsed into non-overlapping ones.
- Repeated operation: compare the next interval to the currently active merged interval.
- Useful structure: sorted starts.

## Pattern Choice

- Primary: Sort by start and sweep.
- Secondary: No heavier structure is needed.

## Why This Matches The Framework

The framework says intervals become easy after sorting because overlap becomes a local decision.

## Invariant

The output list stays sorted and non-overlapping, and its last interval is the active merge target.

## Skeleton Plan

1. Sort intervals by start.
2. If the next interval does not overlap, append it.
3. Otherwise extend the end of the last merged interval.

## Complexity

Time `O(n log n)` for sorting.

## Common Pitfalls

- Sorting is the key step.
- Be explicit about whether touching boundaries count as overlap.
- Watch for accidental aliasing if mutating interval lists in place.

## Python Solution

```python
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda interval: interval[0])
        merged = []

        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        return merged
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
