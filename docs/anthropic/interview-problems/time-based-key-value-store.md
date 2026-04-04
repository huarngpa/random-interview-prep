# Time Based Key-Value Store

- LeetCode: [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)
- Category: `Public-signal closest match`
- Why it is here: this is one of the cleanest LeetCode proxies for progressive in-memory store design.

## Framework Classification

- Input structure: repeated writes and historical reads
- Output asks for the latest value at or before a timestamp
- Repeated operation: search one key's ordered history
- Remembered state: per-key append-only timeline

## Pattern Choice

- Primary: hash map plus binary search
- Secondary: design around repeated operations

## Invariant

Each key's history remains sorted by timestamp, so rightmost `<= timestamp` lookup is valid.

## Skeleton Plan

1. Store a list of `(timestamp, value)` for each key.
2. Append on `set`.
3. Binary search on `get`.
4. Return the rightmost valid value.

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

## Common Pitfalls

- Returning only exact matches instead of rightmost valid history
- Forgetting this depends on monotonic timestamps
- Re-scanning linearly on every `get`

## Related Docs

- [Algorithm Framework](../algorithm-framework.md)
