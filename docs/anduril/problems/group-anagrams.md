# Group Anagrams

- Difficulty: `MEDIUM`
- Frequency In CSV: `88.3`
- Acceptance Rate In CSV: `0.7092885297664818`
- Source: [LeetCode](https://leetcode.com/problems/group-anagrams)
- Topics: `Array, Hash Table, String, Sorting`

## Framework Classification

- Input structure: list of strings.
- Output asks for equivalence classes.
- Repeated operation: compute a canonical signature for each word.
- Remembered state: map from signature to grouped words.

## Pattern Choice

- Primary: Hash map keyed by sorted word or fixed-size character-count tuple.
- Secondary: Sorting is simplest; count-tuples are slightly more optimal.

## Why This Matches The Framework

The framework points to grouping with a hash map. The real decision is choosing a canonical representation that makes equivalent words collide.

## Invariant

Every processed word is stored under a signature that uniquely identifies its anagram class.

## Skeleton Plan

1. Choose a signature strategy.
2. For each word, compute the signature and append it into the matching bucket.
3. Return all buckets at the end.

## Complexity

Depends on signature choice: sorted signatures are about `O(n * k log k)`, count signatures about `O(n * k)`.

## Common Pitfalls

- Do not use a mutable list as a dictionary key.
- Order of groups usually does not matter unless the prompt says so.
- The signature should be the only thing that decides bucket membership.

## Python Solution

```python
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for word in strs:
            counts = [0] * 26
            for ch in word:
                counts[ord(ch) - ord("a")] += 1
            groups[tuple(counts)].append(word)

        return list(groups.values())
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
