# Basic Calculator II

- Difficulty: `MEDIUM`
- Frequency In CSV: `63.2`
- Acceptance Rate In CSV: `0.45811455267149553`
- Source: [LeetCode](https://leetcode.com/problems/basic-calculator-ii)
- Topics: `Math, String, Stack`

## Framework Classification

- Input structure: expression string with precedence but no parentheses.
- Output asks for evaluated result.
- Repeated operation: collapse high-precedence terms as soon as they are known.
- Remembered state: current number, previous operator, and a stack or running last term.

## Pattern Choice

- Primary: Single pass with operator handling and stack.
- Secondary: Constant-space last-term variants are also common.

## Why This Matches The Framework

The framework points to string parsing plus stack when precedence needs to be preserved locally.

## Invariant

Any multiplication or division affecting a term is resolved before that term is committed to the final sum.

## Skeleton Plan

1. Scan the string and build the current number.
2. When you hit an operator or the end, apply the previous operator.
3. Push additive terms and collapse multiplicative ones immediately.
4. Sum the final terms.

## Complexity

Time `O(n)`, space `O(n)` or `O(1)` with optimized state.

## Common Pitfalls

- Skip spaces carefully.
- Do not forget to flush the last number.
- LeetCode integer division truncates toward zero.

## Python Solution

```python
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = "+"

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in "+-*/" or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))

                op = ch
                num = 0

        return sum(stack)
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
