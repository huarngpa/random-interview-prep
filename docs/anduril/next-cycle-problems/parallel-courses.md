# Parallel Courses

- LeetCode: [1136. Parallel Courses](https://leetcode.com/problems/parallel-courses/)
- Why It Is Likely: this is another clean next-step evolution of Anduril's dependency family. It keeps the DAG flavor but adds layer counting rather than just feasibility or ordering.

## Pattern Family

- topological sort
- BFS over DAG levels

## Framework Classification

- Input structure: prerequisite graph
- Output asks for the minimum number of semesters or layers
- Repeated operation: process one frontier of available courses at a time
- Hidden structure: the queue frontier corresponds to one semester

## Principle To Internalize

This is still topological sorting, but the answer is not just:

- can I process everything?

It is:

- how many waves of zero-indegree work are needed?

That means the BFS layers themselves are the answer.

## Solving Walkthrough

1. Build the graph and indegree array.
2. Initialize the queue with all zero-indegree nodes.
3. Process the queue one layer at a time.
4. Each layer is one semester.
5. If not all nodes are processed, there is a cycle.

## Python Solution

```python
from collections import defaultdict, deque


class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0] * (n + 1)

        for prev_course, next_course in relations:
            graph[prev_course].append(next_course)
            indegree[next_course] += 1

        queue = deque(i for i in range(1, n + 1) if indegree[i] == 0)
        semesters = 0
        taken = 0

        while queue:
            semesters += 1
            for _ in range(len(queue)):
                course = queue.popleft()
                taken += 1
                for neighbor in graph[course]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

        return semesters if taken == n else -1
```

## Complexity

- Time: `O(V + E)`
- Space: `O(V + E)`

## Historical Connection

This sits directly on top of:

- `Course Schedule`
- `Course Schedule II`

It is the same base pattern with one extra operational quantity layered on top.
