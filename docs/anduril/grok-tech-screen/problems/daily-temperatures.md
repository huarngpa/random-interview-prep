# Daily Temperatures

- LeetCode: [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
- Why It Is Likely: this is a very common monotonic-stack Medium and a nice second-shape complement to grid problems.

## Why Anduril Asks This

Even though the story is about temperatures, the real pattern is:

- you receive a stream of values
- some earlier items are unresolved
- a new value may resolve several old items at once

That is a very real software pattern in operational systems:

- alerts waiting for a stronger signal
- jobs waiting for a threshold event
- metrics waiting to be superseded
- queues of unresolved observations

Anduril likely cares less about weather and more about whether you know how to maintain an ordered frontier efficiently.

## Framework Classification

- Input structure: array with next-greater queries
- Output asks for distance to the next larger value
- Repeated operation: resolve older indices when a better value arrives
- Remembered state: monotonic stack of unresolved indices

## Pattern Choice

- Primary: monotonic decreasing stack
- Secondary: right-to-left dynamic formulations are possible but less standard

## Principle To Internalize

The stack holds indices whose answer we still do not know.

It is kept in decreasing temperature order, so when a warmer day arrives:

- it can resolve the top
- and maybe several more beneath it

Each index is pushed once and popped once.

That is why the whole algorithm is linear.

## Solving Walkthrough

1. Initialize an answer array full of `0`s.
2. Create an empty stack of indices.
3. Walk left to right through the temperatures.
4. While the current temperature is warmer than the index at the top of the stack, pop and fill in its answer.
5. Push the current index.
6. Leave any unresolved indices as `0`.

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

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Interview Notes

- Say clearly that the stack stores indices, not values.
- Name the invariant: temperatures at stack indices are monotonic decreasing.
- This is a great place to sound confident by explaining why the time is still linear.
