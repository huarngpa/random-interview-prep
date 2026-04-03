# Search Suggestions System

- Difficulty: `MEDIUM`
- Frequency In CSV: `74.8`
- Acceptance Rate In CSV: `0.6505022273267432`
- Source: [LeetCode](https://leetcode.com/problems/search-suggestions-system)
- Topics: `Array, String, Binary Search, Trie, Sorting, Heap (Priority Queue)`

## Framework Classification

- Input structure: products plus progressively longer query prefixes.
- Output asks for top prefix matches after each keystroke.
- Repeated operation: narrow the valid matching range as the prefix grows.
- Remembered state: sorted products or trie path.

## Pattern Choice

- Primary: Sort products and binary search the matching range for each prefix.
- Secondary: Trie is also valid, especially in a design framing.

## Why This Matches The Framework

The framework prefers imposing order first. Sorted products make each prefix a range-query problem.

## Invariant

At each prefix length, the chosen range contains only products matching that prefix.

## Skeleton Plan

1. Sort products once.
2. For each prefix, binary search the left boundary.
3. Collect up to three matching products from that point.
4. Repeat as the prefix grows.

## Complexity

Typically `O(n log n + m log n + output)`.

## Common Pitfalls

- Still validate the prefix when collecting up to three suggestions.
- Trie is not automatically better for a single query stream.
- Sorting gives the correct lexicographic order for free.

## Python Solution

```python
from bisect import bisect_left


class Solution:
    def suggestedProducts(
        self,
        products: list[str],
        searchWord: str,
    ) -> list[list[str]]:
        products.sort()
        answer = []
        prefix = ""

        for ch in searchWord:
            prefix += ch
            start = bisect_left(products, prefix)
            suggestions = []

            for product in products[start:start + 3]:
                if product.startswith(prefix):
                    suggestions.append(product)

            answer.append(suggestions)

        return answer
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
