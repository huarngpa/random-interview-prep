# Likely Problem Pool

This is the focused problem pool implied by the Grok-style analysis of the Anduril screen.

The core claim is:

- the screen is likely `2` Medium problems in `45` minutes
- the highest-probability categories are arrays, matrices, BFS/DFS, strings, and stack-based processing

That makes the goal very practical:

- solve clean Mediums quickly
- do not get lost in low-frequency specialties

## Most Likely Problem Shapes

### 1. Grid Traversal

Highest-probability examples:

- [Number of Islands](./problems/number-of-islands.md)
- [Rotting Oranges](./problems/rotting-oranges.md)

Why this matters:

- Anduril historically likes matrix and graph problems
- these are easy to re-theme into factory floors, sensor maps, or operational layouts
- they test whether you can identify connected components or wavefront expansion quickly

What to internalize:

- hidden graph in a grid
- BFS vs DFS choice
- visited-state discipline
- multi-source BFS when many things spread at once

### 2. Matrix Traversal / Simulation

Highest-probability examples:

- [Spiral Matrix](./problems/spiral-matrix.md)
- [Game of Life](./problems/game-of-life.md)

Why this matters:

- these are array-heavy and implementation-heavy
- they test whether you can stay organized while mutating or traversing a matrix
- Anduril-style screens seem comfortable with “do the straightforward thing correctly” problems

What to internalize:

- keep explicit boundaries or next-state rules
- avoid off-by-one mistakes
- talk through invariants as you code

### 3. Stack / Ordered State

Highest-probability example:

- [Daily Temperatures](./problems/daily-temperatures.md)

Why this matters:

- this is a clean monotonic-stack representative
- it is a common “pattern recognition” Medium
- it tests whether you know when to maintain a frontier of unresolved items

What to internalize:

- stack stores indices, not just values
- keep a monotonic invariant
- each item is pushed and popped at most once

### 4. String / Hash Map

Highest-probability examples:

- [Group Anagrams](./problems/group-anagrams.md)

Solid supplemental pick:

- `Palindromic Substrings`

Why this matters:

- this is a lighter category that still appears often enough to matter
- it rewards clean mapping, normalization, and iteration
- it is a plausible first problem in a screen

What to internalize:

- define the grouping key clearly
- explain why the chosen key is canonical
- keep implementation boring and correct

## Best Predicted Pairings

If I had to compress the likely screen into pairings, these are the strongest candidates:

### Pairing A

- [Spiral Matrix](./problems/spiral-matrix.md)
- [Rotting Oranges](./problems/rotting-oranges.md)

Why:

- one traversal implementation problem
- one BFS/simulation problem

### Pairing B

- [Number of Islands](./problems/number-of-islands.md)
- [Daily Temperatures](./problems/daily-temperatures.md)

Why:

- one graph problem
- one monotonic-stack problem

### Pairing C

- [Group Anagrams](./problems/group-anagrams.md)
- [Game of Life](./problems/game-of-life.md)

Why:

- one easy-to-start hash problem
- one more detail-heavy matrix simulation

## What Seems Less Likely For This Specific Screen

Possible, but not where I would spend the first prep hours:

- heavy DP
- heap-heavy scheduling
- trees
- linked lists
- deep hard-problem reframes

Those are still worth knowing at the broader loop level, but this narrower screen prep pack should stay disciplined.
