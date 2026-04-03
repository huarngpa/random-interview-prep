# Basic Calculator

- Difficulty: `HARD`
- Frequency In CSV: `53.9`
- Acceptance Rate In CSV: `0.45589654652961087`
- Source: [LeetCode](https://leetcode.com/problems/basic-calculator)
- Topics: `Math, String, Stack, Recursion`

## Framework Classification

- Input structure: arithmetic expression with nested parentheses.
- Output asks for evaluated result.
- Repeated operation: evaluate one scope while preserving the outer scope state.
- Remembered state: running total, current sign, and stack or recursion frames.

## Pattern Choice

- Primary: Stack-based parsing or recursive descent.
- Secondary: Compared with Calculator II, parentheses introduce nested scopes.

## Why This Matches The Framework

The framework points to stack or recursion when nested structure matters. Parentheses tell you exactly when to save and restore evaluation state.

## Invariant

Each stack frame or recursive call completely represents one parenthesized evaluation scope.

## Skeleton Plan

1. Scan the expression and build numbers.
2. Apply signs to completed numbers.
3. On `(`, push or recurse into a new scope.
4. On `)`, resolve the current scope and fold it into the parent scope.

## Complexity

Time `O(n)`, space `O(n)`.

## Common Pitfalls

- This version mostly needs `+`, `-`, and parentheses handling.
- Skip spaces.
- Choose either explicit stack state or recursive parsing up front.

## Python Solution

```python
class Solution:
    def calculate(self, s: str) -> int:
        total = 0
        num = 0
        sign = 1
        stack = []

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in "+-":
                total += sign * num
                num = 0
                sign = 1 if ch == "+" else -1
            elif ch == "(":
                stack.append(total)
                stack.append(sign)
                total = 0
                sign = 1
            elif ch == ")":
                total += sign * num
                num = 0
                total *= stack.pop()
                total += stack.pop()

        return total + sign * num
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
