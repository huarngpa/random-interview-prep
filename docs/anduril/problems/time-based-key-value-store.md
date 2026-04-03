# Time Based Key-Value Store

- Difficulty: `MEDIUM`
- Frequency In CSV: `53.9`
- Acceptance Rate In CSV: `0.49366388355657287`
- Source: [LeetCode](https://leetcode.com/problems/time-based-key-value-store)
- Topics: `Hash Table, String, Binary Search, Design`

## Framework Classification

- Input structure: repeated writes and historical reads by key.
- Output asks for the latest value at or before a timestamp.
- Repeated operation: search within one key's ordered history.
- Remembered state: per-key append-only timeline.

## Pattern Choice

- Primary: Hash map of sorted timestamped values plus binary search.
- Secondary: The design relies on timestamps arriving in nondecreasing order for each key.

## Why This Matches The Framework

The framework says store per-key history once, then answer ordered queries with binary search.

## Invariant

Each key's timeline remains sorted, so rightmost `<= timestamp` search is valid.

## Skeleton Plan

1. On `set`, append `(timestamp, value)` to that key's timeline.
2. On `get`, binary search for the rightmost timestamp not exceeding the query time.
3. Return the associated value or the empty string if none exists.

## Complexity

Set `O(1)` amortized, get `O(log n)` for one key.

## Common Pitfalls

- The binary search wants the rightmost valid item, not just an exact match.
- Per-key storage avoids scanning irrelevant entries.
- This is a design problem, so think about repeated operations first.

## Python Solution

```python
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store.get(key, [])
        left, right = 0, len(arr) - 1
        answer = ""

        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                answer = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return answer
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
