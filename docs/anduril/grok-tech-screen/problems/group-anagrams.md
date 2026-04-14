# Group Anagrams

- LeetCode: [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- Why It Is Likely: this is a clean hash-map grouping Medium and a realistic first problem in a short screen.

## Why Anduril Asks This

This one is not manufacturing-shaped on the surface, but the underlying skill still matters:

- choose a canonical representation
- normalize noisy input into a stable key
- group related records efficiently

That shows up everywhere in internal platforms:

- grouping part identifiers
- deduplicating work items
- clustering records by normalized structure
- building indexes for operational data

So the real question is:

- can you create the right key for grouping?

## Framework Classification

- Input structure: list of strings
- Output asks for grouped equivalence classes
- Repeated operation: map each string to a canonical key
- Remembered state: dictionary from key to bucket

## Pattern Choice

- Primary: hash map with sorted-string key
- Secondary: a 26-count tuple key is faster but slightly more complex

## Principle To Internalize

Anagrams are equal after normalization.

So the real problem is not "compare every pair of strings."

It is:

- define one canonical representation for all anagrams
- use that representation as a dictionary key

The easiest canonical representation is the sorted string.

## Solving Walkthrough

1. Create a dictionary from canonical key to list of words.
2. For each word, sort its characters to build the key.
3. Append the word into that bucket.
4. Return the dictionary values.

## Python Solution

```python
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)

        return list(groups.values())
```

## Complexity

- Time: `O(n * k log k)` where `k` is average word length
- Space: `O(n * k)`

## Interview Notes

- Say "canonical key" early.
- Mention that a character-count tuple is a nice follow-up optimization.
- This is a good place to sound calm and clean rather than over-engineered.
