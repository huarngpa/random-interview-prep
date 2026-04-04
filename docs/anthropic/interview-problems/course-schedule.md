# Course Schedule

- LeetCode: [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
- Category: `Role-aligned proxy`
- Why it is here: dependency graphs and allocation ordering map well to workload orchestration and scheduling systems.

## Framework Classification

- Input structure: directed dependency graph
- Output asks whether a valid order exists
- Repeated operation: remove satisfied prerequisites
- Remembered state: indegrees

## Pattern Choice

- Primary: topological sort
- Secondary: DFS cycle detection is also valid

## Invariant

Every node dequeued from the zero-indegree frontier already has all prerequisites satisfied.

## Skeleton Plan

1. Build adjacency lists and indegrees.
2. Queue all zero-indegree nodes.
3. Process neighbors and decrement indegrees.
4. If all nodes are processed, there is no cycle.

## Python Solution

```python
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        seen = 0

        while queue:
            node = queue.popleft()
            seen += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return seen == numCourses
```

## Common Pitfalls

- Reversing edge direction
- Forgetting that this is a cycle-detection problem
- Using only a visited set in DFS without tracking the recursion stack

## Related Docs

- [Algorithm Framework](../algorithm-framework.md)
