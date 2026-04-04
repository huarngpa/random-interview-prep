# Level Three Problems

This is the third practice set.

The goal here is not just pattern fluency. It is pattern recognition under noise.

These problems are still standard interview problems, but they are less “pure” than level two:

- patterns are mixed together
- the problem statement hides the structure a bit more
- implementation details get more annoying
- there are more opportunities to choose the wrong abstraction

## The Set

### 1. Insert Interval

- LeetCode: `57`
- Pattern: intervals with case handling
- Why it matters: same family as merge intervals, but less cleanly packaged

### 2. Top K Frequent Elements

- LeetCode: `347`
- Pattern: hash map + heap
- Why it matters: combines counting with prioritized extraction

### 3. Course Schedule II

- LeetCode: `210`
- Pattern: topological sort returning an actual order
- Why it matters: same dependency graph idea, but with a stronger output requirement

### 4. Redundant Connection

- LeetCode: `684`
- Pattern: union find on a graph
- Why it matters: teaches when union find is cleaner than traversal

### 5. Word Break

- LeetCode: `139`
- Pattern: memoization / DP on string state
- Why it matters: teaches repeated subproblems in parsing-style problems

### 6. Contiguous Array

- LeetCode: `525`
- Pattern: transformed prefix sum
- Why it matters: teaches how to transform a condition into a prefix-state equality

### 7. Accounts Merge

- LeetCode: `721`
- Pattern: union find + mapping
- Why it matters: a more realistic union-find problem with identity stitching

### 8. Network Delay Time

- LeetCode: `743`
- Pattern: shortest path / Dijkstra
- Why it matters: a good first weighted-graph problem

### 9. Pacific Atlantic Water Flow

- LeetCode: `417`
- Pattern: graph traversal from multiple sources
- Why it matters: teaches a reversal trick that simplifies search

### 10. Task Scheduler

- LeetCode: `621`
- Pattern: greedy / counting / heap flavor
- Why it matters: good practice for scheduling-style reasoning

## Recommended Order

1. Insert Interval
2. Top K Frequent Elements
3. Course Schedule II
4. Redundant Connection
5. Word Break
6. Contiguous Array
7. Pacific Atlantic Water Flow
8. Network Delay Time
9. Accounts Merge
10. Task Scheduler

## Why This Is Level Three

These problems start forcing better judgment.

Examples:

- `Top K Frequent Elements` is not just a heap problem; it starts as counting
- `Contiguous Array` is not obviously prefix sum until you transform `0` and `1`
- `Accounts Merge` is not obviously union find until you model shared emails as connectivity
- `Pacific Atlantic Water Flow` becomes easier only after you reverse the direction of thought
- `Task Scheduler` is easy to overcomplicate if you do not recognize the counting structure

## What You Should Practice Here

At this stage, practice the following:

- naming the pattern before coding
- defending why one pattern is better than a tempting alternative
- stating the invariant clearly
- describing complexity without hand-waving
- walking edge cases before you run out of time

## Signs You Are Ready For Level Four

You are ready for a harder set when you can:

- identify the right family within 2 to 3 minutes
- explain why the obvious wrong approach fails
- code the main skeleton without getting lost
- debug edge cases without rewriting from scratch

## Mental Shift

Level one asks:

- can I code basic patterns?

Level two asks:

- do I know the canonical representatives?

Level three asks:

- can I still see the pattern when the problem is disguised?
