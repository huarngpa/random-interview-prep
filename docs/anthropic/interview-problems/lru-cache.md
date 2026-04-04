# LRU Cache

- LeetCode: [146. LRU Cache](https://leetcode.com/problems/lru-cache/)
- Category: `Role-aligned proxy`
- Why it is here: Anthropic's role language points toward practical infrastructure systems, where cache semantics and stateful service design matter.

## Framework Classification

- Input structure: stateful object with repeated `get` and `put`
- Output asks for correct eviction and lookup behavior
- Repeated operation: move recently used keys to the front
- Remembered state: hash map plus recency ordering

## Pattern Choice

- Primary: doubly linked list plus hash map
- Secondary: `OrderedDict` is a Python shortcut, but the core idea is still the same

## Invariant

The linked structure is always in recency order, and the hash map always points to live nodes in that structure.

## Skeleton Plan

1. Keep a map from key to node.
2. Keep a doubly linked list ordered by recency.
3. On access, move the node to the front.
4. On overflow, evict from the tail.

## Python Solution

```python
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

## Common Pitfalls

- Forgetting that both `get` and `put` update recency
- Evicting the wrong side of the ordering
- Treating this like a pure algorithm problem instead of a stateful object design problem

## Related Docs

- [Algorithm Framework](../algorithm-framework.md)
