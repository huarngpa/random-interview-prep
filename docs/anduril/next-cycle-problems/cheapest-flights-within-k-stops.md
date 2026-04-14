# Cheapest Flights Within K Stops

- LeetCode: [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
- Why It Is Likely: this is a strong candidate for the "one harder graph reframe" slot in a new cycle. It combines shortest-path instincts with an extra state dimension.

## Pattern Family

- graph shortest path with bounded state
- DP / Bellman-Ford style relaxation

## Framework Classification

- Input structure: weighted directed graph with a stop constraint
- Output asks for the minimum cost under bounded path length
- Repeated operation: relax edges while limiting how many segments are used
- Hidden structure: cost is not enough state by itself, because stop count also matters

## Principle To Internalize

The trap is to think:

- "shortest path means plain Dijkstra"

But the stop constraint changes the state.

One clean way to solve it is:

- Bellman-Ford style dynamic programming
- relax all edges `k + 1` times

That directly matches the constraint and avoids more complicated stateful heaps.

## Solving Walkthrough

1. Initialize best-known costs with `src = 0`.
2. For each allowed number of edges from `0` to `k`, make one relaxation pass over all flights.
3. Use a copied previous array each round so one round does not accidentally use improvements from the same round.
4. Return the best cost to `dst`, or `-1` if unreachable.

## Python Solution

```python
class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: list[list[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            next_prices = prices[:]
            for start, end, price in flights:
                if prices[start] == float("inf"):
                    continue
                next_prices[end] = min(next_prices[end], prices[start] + price)
            prices = next_prices

        return -1 if prices[dst] == float("inf") else prices[dst]
```

## Complexity

- Time: `O((k + 1) * E)`
- Space: `O(V)`

## Historical Connection

This is a plausible successor to the harder historical questions because it requires:

- recognizing that the obvious graph template is incomplete
- adding the right extra state dimension
- choosing a solution shape that matches the constraint cleanly
