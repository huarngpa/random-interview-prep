# Valid Parentheses

- Difficulty: `EASY`
- Frequency In CSV: `53.9`
- Acceptance Rate In CSV: `0.4232285107271765`
- Source: [LeetCode](https://leetcode.com/problems/valid-parentheses)
- Topics: `String, Stack`

## Framework Classification

- Input structure: token stream with nested matching rules.
- Output asks whether the nesting is valid.
- Repeated operation: match each closing token with the latest unmatched opener.
- Remembered state: stack of unmatched opening brackets.

## Pattern Choice

- Primary: Stack.
- Secondary: A closing-to-opening map makes the checks cleaner.

## Why This Matches The Framework

The framework points to stack for nested rollback structure. Closings must match in reverse order of openings.

## Invariant

The stack stores unmatched opening brackets in the exact order they must close.

## Skeleton Plan

1. Push opening brackets.
2. On a closing bracket, ensure the stack top matches the expected opener.
3. Return true only if the stack is empty after the full scan.

## Complexity

Time `O(n)`, space `O(n)`.

## Common Pitfalls

- Extra closing brackets should fail immediately.
- An empty stack at the end is required.
- This is a foundational stack pattern worth memorizing.

## Python Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack or stack.pop() != pairs[ch]:
                    return False

        return not stack
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
