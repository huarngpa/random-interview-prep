# Anduril Study Pack

This folder now has two purposes:

1. Document the historical Anduril problem set from the public CSV.
2. Infer what the next hiring cycle is likely to ask, then turn that into a practical study guide.

There is now also a narrower tech-screen sprint pack at [./grok-tech-screen](./grok-tech-screen), focused specifically on the "two Mediums in 45 minutes" preparation angle.

The historical set matters because it shows the problem families Anduril has favored over time. The prediction track matters because interviews rarely repeat the exact same questions forever. More often, they keep the same taste and change the skin.

## Source Data

- Repo folder: [Anduril](https://github.com/liquidslr/interview-company-wise-problems/tree/main/Anduril)
- Historical CSV: [5. All.csv](https://github.com/liquidslr/leetcode-company-wise-problems/blob/main/Anduril/5.%20All.csv)
- Recent-window CSVs:
  - [1. Thirty Days.csv](https://raw.githubusercontent.com/liquidslr/interview-company-wise-problems/main/Anduril/1.%20Thirty%20Days.csv)
  - [2. Three Months.csv](https://raw.githubusercontent.com/liquidslr/interview-company-wise-problems/main/Anduril/2.%20Three%20Months.csv)
  - [3. Six Months.csv](https://raw.githubusercontent.com/liquidslr/interview-company-wise-problems/main/Anduril/3.%20Six%20Months.csv)

As of April 13, 2026, the `Thirty Days` file appears empty, so the strongest usable signal is still the three-month, six-month, and all-time trend rather than a sharp recent spike.

## What The Historical Set Says

The Anduril set is not random. It clusters around a few families:

- grid and graph traversal with twists
- dependency graphs and topological ordering
- heaps, schedulers, and dynamic priority handling
- interval reasoning and ordered greedy
- mutable-state design problems
- one or two genuine hard reframe problems

That is a very particular taste profile.

It is much less "grind every classic LeetCode category" and much more:

- operationally flavored graph problems
- stateful objects with evolving API requirements
- scheduling and resource-allocation logic
- geometry or DP hards that still have strong structure

## Historical Cluster Analysis

### 1. Grid / Graph Traversal With An Extra Idea

Historical examples:

- [Number of Islands](./problems/number-of-islands.md)
- [Making A Large Island](./problems/making-a-large-island.md)
- [Number of Distinct Islands](./problems/number-of-distinct-islands.md)
- [Rotting Oranges](./problems/rotting-oranges.md)
- [Minesweeper](./problems/minesweeper.md)
- [Snakes and Ladders](./problems/snakes-and-ladders.md)

Interpretation:

- Anduril seems to like graph thinking that begins with familiar BFS/DFS but then adds one more structural wrinkle.
- The wrinkle is often one of:
  - state encoding
  - component labeling
  - shape/signature tracking
  - multi-source expansion
  - local change on top of global connectivity

### 2. Dependency And Ordering Problems

Historical examples:

- [Course Schedule](./problems/course-schedule.md)
- [Course Schedule II](./problems/course-schedule-ii.md)

Interpretation:

- This suggests comfort with DAGs, constraints, build-order logic, and "what becomes available next?" reasoning.
- That is a very natural fit for a company that likely cares about planning, orchestration, and sequencing under real constraints.

### 3. Heap / Scheduler / Streaming State

Historical examples:

- [Find Median from Data Stream](./problems/find-median-from-data-stream.md)
- [Merge k Sorted Lists](./problems/merge-k-sorted-lists.md)
- [Search Suggestions System](./problems/search-suggestions-system.md)

Interpretation:

- They appear to like problems where the main challenge is maintaining a frontier of "best next candidates" under changing conditions.
- That taste often generalizes into scheduling, assignment, and resource arbitration questions.

### 4. Ordered Greedy And Interval Thinking

Historical examples:

- [Video Stitching](./problems/video-stitching.md)
- [Merge Intervals](./problems/merge-intervals.md)
- [Heaters](./problems/heaters.md)

Interpretation:

- These are all in the family of:
  - create order first
  - then reason locally
- This points toward event processing, coverage, reservations, resource windows, and sweep-line style thinking.

### 5. Stateful Design And API Logic

Historical examples:

- [Time Based Key-Value Store](./problems/time-based-key-value-store.md)
- [Basic Calculator II](./problems/basic-calculator-ii.md)
- [Insert into a Sorted Circular Linked List](./problems/insert-into-a-sorted-circular-linked-list.md)

Interpretation:

- This is a sign they are comfortable asking for object behavior, mutable state, and implementation discipline, not just single-shot algorithms.
- These problems reward correctness, edge-case handling, and state design more than trick recognition.

### 6. One Genuine Hard Reframe

Historical examples:

- [Maximum Number of Visible Points](./problems/maximum-number-of-visible-points.md)
- [Race Car](./problems/race-car.md)

Interpretation:

- The historical set suggests that at least one question family may ask for a sharper reframe:
  - geometry reduced to sorting and sliding window
  - DP derived from structure
  - answer-space reasoning

This does not look like pure competitive-programming chaos.

It looks more like:

- "We still want hard problems, but we want them to have a recognizable shape."

## What A New Hiring Cycle Is Likely To Change

If Anduril is in a new cycle, the safest assumption is:

- the skin changes more than the taste

That means they are more likely to ask:

- new graph problems that feel like the old graph problems
- new scheduler problems that feel like the old heap problems
- new stateful designs that feel like the old mutable-object questions

They are less likely to suddenly pivot into:

- obscure string automata
- random combinatorics
- pure math olympiad problems
- deep segment tree or Fenwick tree specialization

## Predicted Next-Cycle Problem Families

### Most Likely

1. Graph / grid with a stronger twist
2. Heap-based scheduling and allocation
3. DAG ordering with more operational framing
4. Stateful object design with richer mutation semantics
5. Intervals or event-based resource reasoning

### Still Plausible

1. Shortest-path state search
2. Multi-source traversal
3. Binary-search-on-answer optimization
4. Union-find with identity stitching

### Less Likely

1. Pure heavy-string trick questions
2. Purely mathematical proofs with little operational intuition
3. Very specialized data structures with no obvious systems flavor

## Study Guide

The best way to study this set is not to chase 100 random Anduril-adjacent problems.

Study in layers.

### Layer 1: Understand The Historical Taste

Use the historical notes in [./problems](./problems) to understand what they have already liked.

Priority historical problems:

- [Number of Islands](./problems/number-of-islands.md)
- [Course Schedule](./problems/course-schedule.md)
- [Course Schedule II](./problems/course-schedule-ii.md)
- [Time Based Key-Value Store](./problems/time-based-key-value-store.md)
- [Merge Intervals](./problems/merge-intervals.md)
- [Find Median from Data Stream](./problems/find-median-from-data-stream.md)
- [Making A Large Island](./problems/making-a-large-island.md)

### Layer 2: Practice The Predicted Next-Cycle Set

Use the notes in [./next-cycle-problems](./next-cycle-problems) to practice the likely next variants of those same families.

Priority next-cycle problems:

- [Pacific Atlantic Water Flow](./next-cycle-problems/pacific-atlantic-water-flow.md)
- [Alien Dictionary](./next-cycle-problems/alien-dictionary.md)
- [Single-Threaded CPU](./next-cycle-problems/single-threaded-cpu.md)
- [Process Tasks Using Servers](./next-cycle-problems/process-tasks-using-servers.md)
- [Design In-Memory File System](./next-cycle-problems/design-in-memory-file-system.md)

### Layer 3: Hardening

Once the core patterns feel stable, push into the harder predicted variants:

- [Swim in Rising Water](./next-cycle-problems/swim-in-rising-water.md)
- [Cheapest Flights Within K Stops](./next-cycle-problems/cheapest-flights-within-k-stops.md)
- [Accounts Merge](./next-cycle-problems/accounts-merge.md)

## Tech Screen Sprint Pack

If you want the narrower, tactical prep view for a short HackerRank-style screen, use:

- [Tech Screen Notes](./grok-tech-screen/README.md)
- [Likely Problem Pool](./grok-tech-screen/likely-problem-pool.md)
- [45-Minute Screen Strategy](./grok-tech-screen/screen-strategy.md)
- [48-Hour Study Plan](./grok-tech-screen/study-plan.md)

## How To Use The Problem Notes

Each predicted problem file includes:

- why it is likely given Anduril's history
- the framework classification
- the principle to internalize
- a solving walkthrough
- a Python reference solution

The intended use is:

1. Read the problem statement on LeetCode.
2. Try to classify it before opening the note.
3. Use the note to compare your pattern recognition and invariant.
4. Implement from memory.
5. Revisit the principle section later until the recognition becomes fast.

## Historical Problems

This is the original public set, preserved as reference.

- `MEDIUM` [Number of Islands](./problems/number-of-islands.md)
- `HARD` [Maximum Number of Visible Points](./problems/maximum-number-of-visible-points.md)
- `MEDIUM` [Video Stitching](./problems/video-stitching.md)
- `MEDIUM` [Group Anagrams](./problems/group-anagrams.md)
- `MEDIUM` [Course Schedule](./problems/course-schedule.md)
- `EASY` [Shortest Word Distance](./problems/shortest-word-distance.md)
- `MEDIUM` [Heaters](./problems/heaters.md)
- `MEDIUM` [Daily Temperatures](./problems/daily-temperatures.md)
- `MEDIUM` [Course Schedule II](./problems/course-schedule-ii.md)
- `HARD` [Find Median from Data Stream](./problems/find-median-from-data-stream.md)
- `MEDIUM` [Search Suggestions System](./problems/search-suggestions-system.md)
- `HARD` [Making A Large Island](./problems/making-a-large-island.md)
- `MEDIUM` [Merge Intervals](./problems/merge-intervals.md)
- `MEDIUM` [Flatten Binary Tree to Linked List](./problems/flatten-binary-tree-to-linked-list.md)
- `MEDIUM` [Shortest Word Distance II](./problems/shortest-word-distance-ii.md)
- `MEDIUM` [Basic Calculator II](./problems/basic-calculator-ii.md)
- `MEDIUM` [Flip Equivalent Binary Trees](./problems/flip-equivalent-binary-trees.md)
- `HARD` [Merge k Sorted Lists](./problems/merge-k-sorted-lists.md)
- `EASY` [Valid Parentheses](./problems/valid-parentheses.md)
- `MEDIUM` [Number of Distinct Islands](./problems/number-of-distinct-islands.md)
- `MEDIUM` [Rotting Oranges](./problems/rotting-oranges.md)
- `MEDIUM` [Minesweeper](./problems/minesweeper.md)
- `EASY` [Move Zeroes](./problems/move-zeroes.md)
- `MEDIUM` [Spiral Matrix](./problems/spiral-matrix.md)
- `MEDIUM` [Time Based Key-Value Store](./problems/time-based-key-value-store.md)
- `MEDIUM` [Insert into a Sorted Circular Linked List](./problems/insert-into-a-sorted-circular-linked-list.md)
- `MEDIUM` [Find the Duplicate Number](./problems/find-the-duplicate-number.md)
- `MEDIUM` [Snakes and Ladders](./problems/snakes-and-ladders.md)
- `MEDIUM` [Search in Rotated Sorted Array](./problems/search-in-rotated-sorted-array.md)
- `MEDIUM` [Game of Life](./problems/game-of-life.md)
- `HARD` [Basic Calculator](./problems/basic-calculator.md)
- `HARD` [Race Car](./problems/race-car.md)

## Framework References

- [Algorithm Framework](../anthropic/algorithm-framework.md)
- [Hard Problem Spells](../anthropic/hard-problem-spells.md)
- [Python Concepts](../anthropic/python-concepts.md)
- [Modern Python](../anthropic/modern-python-for-java.md)
- [UV Test Harness](../anthropic/test-harness.md)
