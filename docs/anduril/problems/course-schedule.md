# Course Schedule

- Difficulty: `MEDIUM`
- Frequency In CSV: `85.6`
- Acceptance Rate In CSV: `0.492343272648647`
- Source: [LeetCode](https://leetcode.com/problems/course-schedule)
- Topics: `Depth-First Search, Breadth-First Search, Graph, Topological Sort`

## Framework Classification

- Input structure: directed prerequisite graph.
- Output asks whether a valid build/order exists.
- Repeated operation: remove or detect dependency cycles.
- Remembered state: indegrees or DFS color states.

## Pattern Choice

- Primary: Topological sort or DFS cycle detection.
- Secondary: Kahn's algorithm is usually the clearest interview answer.

## Why This Matches The Framework

The framework treats prerequisites as dependency ordering. The yes/no version only asks whether the graph is acyclic.

## Invariant

Any node popped from the zero-indegree queue already has all prerequisites satisfied.

## Skeleton Plan

1. Build adjacency list and indegree counts.
2. Queue every node with indegree zero.
3. Process neighbors, decrement indegrees, and enqueue new zero-indegree nodes.
4. If you process all nodes, the schedule is possible.

## Complexity

Time `O(V + E)`, space `O(V + E)`.

## Common Pitfalls

- Edge direction mistakes are common.
- DFS cycle detection needs a recursion-stack state, not just a visited set.
- This version asks for feasibility, not one specific order.

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
        taken = 0

        while queue:
            node = queue.popleft()
            taken += 1

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return taken == numCourses
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
