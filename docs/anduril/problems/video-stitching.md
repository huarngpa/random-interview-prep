# Video Stitching

- Difficulty: `MEDIUM`
- Frequency In CSV: `92.9`
- Acceptance Rate In CSV: `0.5199920692617804`
- Source: [LeetCode](https://leetcode.com/problems/video-stitching)
- Topics: `Array, Dynamic Programming, Greedy`

## Framework Classification

- Input structure: intervals over a target time range.
- Output asks for the minimum number of intervals needed to cover the range.
- Repeated operation: choose the farthest extension available from the current frontier.
- Key constraint: local choices must preserve future reach.

## Pattern Choice

- Primary: Greedy interval coverage.
- Secondary: Dynamic programming exists but is usually heavier than needed.

## Why This Matches The Framework

The framework marks this as intervals plus optimization. Greedy works because among all clips that start in time, the one extending furthest is always the best next move.

## Invariant

At each committed boundary, you have used the minimum number of clips to cover everything up to that point.

## Skeleton Plan

1. Sort clips or preprocess farthest reach by start time.
2. Track the current covered end and the farthest next end.
3. When you exhaust the current boundary, commit one clip and advance.
4. If you cannot extend further before the target, return `-1`.

## Complexity

Typically `O(n log n)` with sorting.

## Common Pitfalls

- This is not a merge-intervals problem; you must minimize clip count.
- Return `-1` as soon as a gap appears.
- The greedy proof depends on always taking the furthest reachable extension.

## Python Solution

```python
class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        clips.sort()
        answer = 0
        current_end = 0
        farthest = 0
        i = 0

        while current_end < time:
            while i < len(clips) and clips[i][0] <= current_end:
                farthest = max(farthest, clips[i][1])
                i += 1

            if farthest == current_end:
                return -1

            answer += 1
            current_end = farthest

        return answer
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
