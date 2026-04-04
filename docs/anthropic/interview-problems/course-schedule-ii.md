# Course Schedule II

- LeetCode: [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
- Category: `Role-aligned proxy`
- Why it is here: same dependency-graph reasoning as Course Schedule, but now you must materialize the actual execution order.

## Framework Classification

- Input structure: directed dependency graph
- Output asks for one valid ordering
- Repeated operation: release nodes with no unmet dependencies
- Remembered state: indegrees and result order

## Pattern Choice

- Primary: topological sort
- Secondary: DFS postorder with cycle detection

## Invariant

Every node appended to the output has indegree zero at append time.

## Skeleton Plan

1. Build the graph and indegrees.
2. Queue all zero-indegree nodes.
3. Pop, append, and unlock neighbors.
4. Return empty if a cycle leaves nodes unprocessed.

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

## Common Pitfalls

- Assuming the order is unique
- Forgetting to handle cycles by returning empty
- Reversing the graph edges

## Related Docs

- [Algorithm Framework](../algorithm-framework.md)
