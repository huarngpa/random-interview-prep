# Flip Equivalent Binary Trees

- Difficulty: `MEDIUM`
- Frequency In CSV: `63.2`
- Acceptance Rate In CSV: `0.696793256042999`
- Source: [LeetCode](https://leetcode.com/problems/flip-equivalent-binary-trees)
- Topics: `Tree, Depth-First Search, Binary Tree`

## Framework Classification

- Input structure: two recursive tree structures.
- Output asks for structural equivalence under local swaps.
- Repeated operation: compare subtrees under two possible child matchings.
- Remembered state: current subtree roots in recursion.

## Pattern Choice

- Primary: Recursive DFS.
- Secondary: Canonical normalization is possible but less direct.

## Why This Matches The Framework

The framework says recursive structure suggests DFS. The current node breaks the problem into the same question on smaller subtrees.

## Invariant

Two subtrees are equivalent if roots match and one of the two child pairings is equivalent.

## Skeleton Plan

1. Handle base cases for nulls and value mismatches.
2. Recursively compare the non-flipped alignment and the flipped alignment.
3. Return true if either alignment works.

## Complexity

Time is proportional to tree size in the common case.

## Common Pitfalls

- You must test both child alignments.
- Base cases should come before recursion.
- Value equality alone is not enough; structure matters.

## Python Solution

```python
from typing import Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (
            self.flipEquiv(root1.left, root2.left)
            and self.flipEquiv(root1.right, root2.right)
        ) or (
            self.flipEquiv(root1.left, root2.right)
            and self.flipEquiv(root1.right, root2.left)
        )
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
