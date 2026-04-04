# Merge Intervals

- LeetCode: [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- Category: `Role-aligned proxy`
- Why it is here: interval reasoning is a basic building block for resource windows, reservations, allocations, and capacity accounting.

## Framework Classification

- Input structure: intervals
- Output asks for collapsed non-overlapping ranges
- Repeated operation: compare the next interval to the current merged range
- Useful structure: sorted starts

## Pattern Choice

- Primary: sort and sweep
- Secondary: local overlap reasoning

## Invariant

The output list is always sorted and non-overlapping, and its last entry is the active merged range.

## Skeleton Plan

1. Sort by start time.
2. Start a merged list.
3. Append if there is no overlap.
4. Otherwise extend the current merged end.

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

## Common Pitfalls

- Forgetting to sort first
- Mis-handling touching boundaries
- Overengineering a problem that becomes simple after ordering

## Related Docs

- [Algorithm Framework](../algorithm-framework.md)
