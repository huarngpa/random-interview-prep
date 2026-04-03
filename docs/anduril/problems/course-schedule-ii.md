# Course Schedule II

- Difficulty: `MEDIUM`
- Frequency In CSV: `79.0`
- Acceptance Rate In CSV: `0.5342347717848052`
- Source: [LeetCode](https://leetcode.com/problems/course-schedule-ii)
- Topics: `Depth-First Search, Breadth-First Search, Graph, Topological Sort`

## Framework Classification

- Input structure: dependency graph.
- Output asks for one valid topological order.
- Repeated operation: release nodes whose prerequisites are fully satisfied.
- Remembered state: indegrees or DFS postorder state.

## Pattern Choice

- Primary: Topological sort.
- Secondary: DFS with postorder and cycle detection also works.

## Why This Matches The Framework

Same framework branch as Course Schedule, except now the result must be an actual valid ordering.

## Invariant

Every node appended to the result has no remaining unmet prerequisites.

## Skeleton Plan

1. Build the graph and indegree counts.
2. Queue all zero-indegree nodes.
3. Pop nodes, append them to the result, and decrement neighbors.
4. If the result is shorter than the number of nodes, a cycle exists.

## Complexity

Time `O(V + E)`, space `O(V + E)`.

## Common Pitfalls

- Do not reverse edge direction.
- Any valid order is acceptable.
- Cycle detection is still required even though you are returning an order.

## Python Solution

```python
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
