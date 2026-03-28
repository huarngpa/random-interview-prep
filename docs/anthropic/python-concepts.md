# Python Concepts For Anthropic Prep

This guide is scoped to what helps you solve interview problems quickly, not everything Python can do.

## The Short Version

If we optimize for speed, the highest-value Python concepts are:

1. Core data structures and their time complexity
2. Functions, scope, and passing data cleanly
3. Iteration patterns over lists, strings, dicts, and sets
4. Sorting with `key=...`
5. `collections` tools like `defaultdict`, `Counter`, and `deque`
6. Writing clean classes for small build problems
7. Heap, stack, queue, and graph patterns
8. Basic file parsing and string processing
9. Error handling and edge-case discipline
10. Simple testing and debugging habits

## What You Actually Need

## 1. Lists, Dicts, Sets, Tuples

These are the foundation for nearly every coding round.

Know these cold:

- `list`: ordered, mutable, great for stacks, scans, two-pointer problems
- `dict`: key/value lookup, counting, grouping, memoization
- `set`: membership checks, deduplication, visited tracking
- `tuple`: immutable records, often used as dictionary keys

Common operations to remember:

```python
nums = [3, 1, 2]
nums.append(4)
last = nums.pop()

counts = {}
counts["a"] = counts.get("a", 0) + 1

seen = set()
seen.add("x")
exists = "x" in seen

pair = (row, col)
```

Time complexity you should be able to say out loud:

- list append/pop at end: usually `O(1)`
- dict lookup/insert: usually `O(1)`
- set lookup/insert: usually `O(1)`
- sorting: `O(n log n)`

## 2. Loops and Iteration

A lot of interview speed comes from being fluent with iteration.

Be comfortable with:

- `for x in items`
- `for i, x in enumerate(items)`
- `for a, b in zip(xs, ys)`
- iterating over `dict.items()`, `dict.keys()`, `dict.values()`
- scanning strings character by character

Examples:

```python
for i, value in enumerate(nums):
    print(i, value)

for key, value in mapping.items():
    print(key, value)
```

## 3. Functions and Scope

You want to break problems into helpers quickly.

Know:

- positional vs keyword arguments
- default arguments
- returning multiple values
- when to use nested helper functions
- avoiding mutable default arguments

Example:

```python
def normalize(word: str) -> str:
    return word.strip().lower()

def split_once(s: str) -> tuple[str, str]:
    left, right = s.split(":", 1)
    return left, right
```

Important pitfall:

```python
# Bad
def add_item(x, items=[]):
    items.append(x)
    return items

# Good
def add_item(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
```

## 4. Strings

Python is excellent for string-heavy problems, and build exercises often involve parsing.

Know:

- slicing: `s[l:r]`
- `split`, `join`, `strip`, `replace`
- checking prefixes/suffixes
- building strings with a list plus `"".join(...)`

Examples:

```python
parts = line.strip().split(",")
name = parts[0]

out = []
for ch in s:
    if ch.isalpha():
        out.append(ch.lower())
result = "".join(out)
```

## 5. Sorting

Many problems become easy once you sort.

Know:

- `sorted(items)`
- `items.sort()`
- `key=` functions
- sorting tuples
- reverse sorting

Examples:

```python
words.sort(key=len)
events = sorted(events, key=lambda event: (event.start, event.end))
```

## 6. Comprehensions

These help you move fast, but only when they stay readable.

Examples:

```python
squares = [x * x for x in nums]
evens = [x for x in nums if x % 2 == 0]
unique_lengths = {len(word) for word in words}
index_by_name = {user.name: user for user in users}
```

Use them for simple transforms, not multi-step logic.

## 7. Collections You Will Probably Use

`collections` is one of the highest-leverage Python modules for interviews.

### `Counter`

```python
from collections import Counter

counts = Counter("banana")
if counts["a"] > 2:
    print("yes")
```

Use for:

- frequency counting
- anagram checks
- top-k frequency prep

### `defaultdict`

```python
from collections import defaultdict

groups = defaultdict(list)
for word in words:
    groups[len(word)].append(word)
```

Use for:

- grouping
- graph adjacency lists
- counting without manual initialization

### `deque`

```python
from collections import deque

queue = deque([start])
node = queue.popleft()
queue.append(next_node)
```

Use for:

- BFS
- queue behavior
- sliding window cases

## 8. Heap, Stack, Queue

These show up constantly.

### Stack

Use a list:

```python
stack = []
stack.append(x)
top = stack.pop()
```

### Queue

Use `deque`, not a list:

```python
from collections import deque

queue = deque()
queue.append(x)
item = queue.popleft()
```

### Heap

Use `heapq`:

```python
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
smallest = heapq.heappop(heap)
```

Know:

- Python `heapq` is a min-heap
- for max-heap behavior, often push negative values

## 9. Recursion, DFS, BFS

Even if the interview is practical, these patterns matter.

Know:

- recursive tree traversal
- DFS with a stack or recursion
- BFS with a deque
- visited sets

Graph skeleton:

```python
from collections import deque

def bfs(graph, start):
    seen = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return seen
```

## 10. Classes For Build Problems

If Anthropic gives a small build problem, you may need to model state cleanly.

You do not need advanced OOP. You do need:

- `class`
- `__init__`
- instance attributes
- small methods with clear responsibilities
- optionally `@dataclass`

Example:

```python
class RateLimiter:
    def __init__(self, limit: int):
        self.limit = limit
        self.counts = {}

    def allow(self, key: str) -> bool:
        used = self.counts.get(key, 0)
        if used >= self.limit:
            return False
        self.counts[key] = used + 1
        return True
```

Also worth knowing:

```python
from dataclasses import dataclass

@dataclass
class Job:
    name: str
    priority: int
```

## 11. Exceptions and Defensive Coding

Build exercises often reward correctness and clean failure modes.

Know:

- `try/except`
- raising `ValueError` for invalid input
- checking for `None`
- guarding edge cases early

Example:

```python
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b
```

## 12. File and Input Handling

If there is a practical exercise, you may need to read structured input quickly.

Know:

- `with open(...) as f`
- iterating line by line
- splitting and parsing
- JSON basics

Examples:

```python
with open("input.txt") as f:
    for line in f:
        line = line.strip()
```

```python
import json

data = json.loads('{"x": 1}')
```

## 13. Testing Habits

Even if they do not ask for full tests, interviewers like seeing quick verification.

Useful habits:

- run a happy-path example
- run 2 to 3 edge cases
- mention complexity
- name assumptions explicitly

Tiny example:

```python
assert normalize(" Hi ") == "hi"
assert normalize("") == ""
```

## 14. Python Standard Library Shortlist

You do not need all of it. Focus on:

- `collections`
- `heapq`
- `itertools`
- `functools`
- `json`
- `math`
- `bisect`

Especially useful:

```python
from itertools import pairwise, combinations
from functools import lru_cache
from bisect import bisect_left, bisect_right
```

## 15. The Most Useful Interview Patterns

These patterns matter more than obscure syntax.

- hash map counting
- group by key
- two pointers
- sliding window
- prefix sums
- interval merge
- BFS/DFS
- heap for top-k or scheduling
- binary search on sorted data
- simple stateful object design

## What Matters Less

You can safely deprioritize these at first:

- metaclasses
- decorators beyond basic familiarity
- generators beyond simple use
- async Python
- advanced typing
- inheritance-heavy OOP
- packaging and virtualenv internals

## Recommended Learning Order

If your Python is rusty, I would refresh in this order:

1. Lists, dicts, sets, strings
2. Loops, functions, comprehensions
3. `Counter`, `defaultdict`, `deque`
4. Sorting, heaps, stacks, queues
5. DFS, BFS, recursion
6. Classes and stateful object modeling
7. File parsing and basic tests

## Best Rule Of Thumb

For interview speed, aim to be good at writing:

- 30 lines of clean list/dict/set logic
- 50 lines of BFS/DFS or heap-based logic
- 80 to 120 lines for a small stateful build problem

That level is usually more valuable than knowing advanced Python tricks.
