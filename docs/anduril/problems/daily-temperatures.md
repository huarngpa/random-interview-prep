# Daily Temperatures

- Difficulty: `MEDIUM`
- Frequency In CSV: `82.5`
- Acceptance Rate In CSV: `0.6736502832589849`
- Source: [LeetCode](https://leetcode.com/problems/daily-temperatures)
- Topics: `Array, Stack, Monotonic Stack`

## Framework Classification

- Input structure: array with next-greater style queries.
- Output asks how far ahead the next warmer/greater value is.
- Repeated operation: resolve old indices when a new value dominates them.
- Remembered state: unresolved candidate indices in monotonic order.

## Pattern Choice

- Primary: Monotonic decreasing stack of indices.
- Secondary: Right-to-left formulations also work.

## Why This Matches The Framework

The framework explicitly tags next-greater problems as monotonic stack problems.

## Invariant

The stack contains unresolved indices in monotonic order, and all popped indices are resolved exactly once.

## Skeleton Plan

1. Initialize the answer array.
2. Scan left to right.
3. While the current value resolves the stack top, pop and fill in the distance.
4. Push the current index.

## Complexity

Time `O(n)`, space `O(n)`.

## Common Pitfalls

- Store indices rather than just values.
- Choose the correct monotonic direction.
- Unresolved indices usually stay at the default answer.

## Python Solution

```python
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)

        return answer
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
