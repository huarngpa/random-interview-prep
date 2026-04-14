# Alien Dictionary

- LeetCode: [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
- Why It Is Likely: this is a natural next-cycle evolution of the historical `Course Schedule` questions. It is still a topological sort, but the graph must be inferred from pairwise constraints.

## Pattern Family

- topological sort
- graph construction from ordering evidence

## Framework Classification

- Input structure: sorted list of words under an unknown alphabet
- Output asks for one valid character ordering
- Repeated operation: infer precedence edges from adjacent words
- Hidden structure: characters are nodes and precedence relations are directed edges

## Principle To Internalize

There are really two problems here:

1. build the graph correctly
2. topologically sort it

Most people focus too early on the topological sort.

The more dangerous part is inferring edges correctly, especially the invalid prefix case.

## Solving Walkthrough

1. Initialize every seen character as a node.
2. Compare adjacent words and find the first differing character.
3. Add an edge from the earlier character to the later character.
4. If a longer word appears before its own prefix, return `""`.
5. Run topological sort and return the result if all characters are included.

## Python Solution

```python
from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        graph = defaultdict(set)
        indegree = {ch: 0 for word in words for ch in word}

        for w1, w2 in zip(words, words[1:]):
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for i in range(min_len):
                if w1[i] != w2[i]:
                    if w2[i] not in graph[w1[i]]:
                        graph[w1[i]].add(w2[i])
                        indegree[w2[i]] += 1
                    break

        queue = deque(ch for ch, deg in indegree.items() if deg == 0)
        order = []

        while queue:
            ch = queue.popleft()
            order.append(ch)
            for neighbor in graph[ch]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return "".join(order) if len(order) == len(indegree) else ""
```

## Complexity

- Time: `O(total characters)`
- Space: `O(unique characters + edges)`

## Historical Connection

This is the same family as:

- `Course Schedule`
- `Course Schedule II`

The new difficulty is not the topo sort itself. It is extracting the graph from partial evidence.
