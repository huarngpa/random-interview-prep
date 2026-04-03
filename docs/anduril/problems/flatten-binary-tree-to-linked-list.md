# Flatten Binary Tree to Linked List

- Difficulty: `MEDIUM`
- Frequency In CSV: `63.2`
- Acceptance Rate In CSV: `0.6851017952147065`
- Source: [LeetCode](https://leetcode.com/problems/flatten-binary-tree-to-linked-list)
- Topics: `Linked List, Stack, Tree, Depth-First Search, Binary Tree`

## Framework Classification

- Input structure: binary tree.
- Output asks for in-place preorder flattening.
- Repeated operation: reconnect nodes in preorder-linked order.
- Remembered state: previous node or subtree tail.

## Pattern Choice

- Primary: DFS preorder rewiring.
- Secondary: Reverse-preorder recursion with a `prev` pointer is a clean pattern.

## Why This Matches The Framework

The framework flags tree traversal plus mutation. The main choice is a traversal order that makes pointer rewiring local.

## Invariant

The already processed portion of the tree is flattened into correct preorder linked-list form.

## Skeleton Plan

1. Choose recursion with a `prev` pointer or iterative preorder with a stack.
2. Rewire pointers so the next node in preorder becomes `right` and `left` becomes `None`.
3. Process the entire tree while preserving references.

## Complexity

Time `O(n)`, space `O(h)` recursion or stack.

## Common Pitfalls

- Preorder is the target order.
- If using reverse preorder recursion, process right before left.
- Do not lose child references before rewiring.

## Python Solution

```python
from typing import Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.prev = None

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            dfs(node.right)
            dfs(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node

        dfs(root)
```

## Related Framework Docs

- [Algorithm Framework](../../anthropic/algorithm-framework.md)
- [Python Concepts](../../anthropic/python-concepts.md)
- [Level One Problems](../../anthropic/level-one-problems.md)
- [UV Test Harness](../../anthropic/test-harness.md)
