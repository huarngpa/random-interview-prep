# Race Car

- Difficulty: `HARD`
- Frequency In CSV: `53.9`
- Acceptance Rate In CSV: `0.4412431163672474`
- Source: [LeetCode](https://leetcode.com/problems/race-car)
- Topics: `Dynamic Programming`

## Framework Classification

- Input structure: one target value with recursive move choices.
- Output asks for a minimum instruction count.
- Repeated operation: solve smaller target distances with overlapping subproblems.
- Remembered state: best answer for each target distance.

## Pattern Choice

- Primary: Dynamic programming with memoization or bottom-up recurrence.
- Secondary: BFS on states exists, but DP is the more structured classic solution.

## Why This Matches The Framework

The framework says optimization plus repeated states points to DP. The structure comes from distances of the form `2^k - 1` after repeated accelerations.

## Invariant

`dp[t]` means the minimum instructions needed to reach exactly distance `t`.

## Skeleton Plan

1. For a target, find the smallest acceleration run that reaches or passes it.
2. If the run lands exactly on target, use that count directly.
3. Otherwise compare overshoot-and-reverse versus reverse-early strategies.
4. Memoize or build the best answer from smaller targets.

## Complexity

Polynomial in target with memoization or bottom-up DP, far better than naive state exploration.

## Common Pitfalls

- The recurrence is the real difficulty.
- This is a good example of deriving DP from structure instead of guessing it.
- Both overshoot and undershoot cases matter.

## Python Solution

```python
from functools import lru_cache


class Solution:
    def racecar(self, target: int) -> int:
        @lru_cache(maxsize=None)
        def dp(t: int) -> int:
            n = t.bit_length()
            full_speed = (1 << n) - 1

            if full_speed == t:
                return n

            best = n + 1 + dp(full_speed - t)
            prev_speed = (1 << (n - 1)) - 1

            for back_steps in range(n - 1):
                reverse_distance = (1 << back_steps) - 1
                remaining = t - (prev_speed - reverse_distance)
                best = min(best, (n - 1) + 1 + back_steps + 1 + dp(remaining))

            return best

        return dp(target)
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
