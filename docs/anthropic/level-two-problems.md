# Level Two Problems

This is the second practice set.

The goal here is to master one canonical representative for each major pattern family.

If level one is about basic fluency, level two is about building a stable mental index:

- what the pattern looks like
- what invariant makes it work
- what implementation skeleton you should reach for immediately

## The Six Cleanest Level Two Problems

### 1. Subarray Sum Equals K

- LeetCode: `560`
- Pattern: prefix sum + hash map
- Why it matters: this is the most important prefix-sum recognition problem

### 2. Merge Intervals

- LeetCode: `56`
- Pattern: intervals + sort/sweep
- Why it matters: this is the cleanest “sort first, then process locally” interval problem

### 3. Kth Largest Element in an Array

- LeetCode: `215`
- Pattern: heap
- Why it matters: this is the simplest high-value heap problem

### 4. Course Schedule

- LeetCode: `207`
- Pattern: topological sort
- Why it matters: this is the canonical dependency graph problem

### 5. Number of Provinces

- LeetCode: `547`
- Pattern: union find
- Why it matters: this is one of the cleanest “dynamic connectivity” problems

### 6. Coin Change

- LeetCode: `322`
- Pattern: memoization / dynamic programming
- Why it matters: this is a classic state-definition DP problem

## Recommended Order

1. Merge Intervals
2. Kth Largest Element in an Array
3. Course Schedule
4. Subarray Sum Equals K
5. Number of Provinces
6. Coin Change

## Why This Order

- `Merge Intervals` is conceptually simple and sharpens your “sort to create structure” instinct
- `Kth Largest` is a clean way to internalize heaps
- `Course Schedule` introduces dependency graphs in a very standard form
- `Subarray Sum Equals K` is the most important prefix-sum leap and is easier once your hash-map fluency is solid
- `Number of Provinces` teaches the union-find mental model with low noise
- `Coin Change` is the right first “real DP” because brute force is obvious and memoization gives a clean improvement

## What “Comfortable” Looks Like

You are ready to move on when you can do these without pattern panic:

- prefix sum: know when to store prior prefix states in a map
- intervals: immediately sort and sweep
- heap: know when the problem is “repeatedly get best candidate”
- topo sort: recognize prerequisites and cycle detection
- union find: recognize repeated merges / connectivity
- DP: define the state before coding

## Invariant Checklist

Before coding each one, say the invariant out loud.

### Subarray Sum Equals K

- The map stores how many times each prefix sum has already appeared.

### Merge Intervals

- The output stays sorted and non-overlapping.

### Kth Largest Element in an Array

- The heap contains the current best `k` candidates.

### Course Schedule

- Every queued course has no unmet prerequisites.

### Number of Provinces

- Every node belongs to exactly one component root.

### Coin Change

- `dp[x]` means the best answer for amount `x`.

## What Comes Next

Once these six feel stable, level three should add:

- mixed-pattern problems
- trickier recognition
- problems where the right pattern is less obvious on first read
