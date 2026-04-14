# Design In-Memory File System

- LeetCode: [588. Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/)
- Why It Is Likely: this is a strong next-cycle design proxy for Anduril's mutable-state and API-behavior questions.

## Pattern Family

- trie-like stateful object design
- path traversal

## Framework Classification

- Input structure: path-based operations over mutable hierarchical state
- Output asks for correct API behavior over time
- Repeated operation: walk a path and mutate or query the final node
- Hidden structure: the file system is a tree keyed by path components

## Principle To Internalize

This is not really an algorithm problem first.

It is a state-modeling problem.

The big question is:

- what object representation makes every operation feel natural?

Here, the clean answer is:

- a node per path segment
- dictionary of children
- file content only on file nodes

## Solving Walkthrough

1. Create a `Node` type with children, content, and file flag.
2. Write one helper to walk a path and create missing nodes when needed.
3. Use that helper for `mkdir`, `addContentToFile`, and `readContentFromFile`.
4. For `ls`, return one filename if the path is a file, otherwise sorted children.

## Python Solution

```python
class Node:
    def __init__(self):
        self.children = {}
        self.content = ""
        self.is_file = False


class FileSystem:
    def __init__(self):
        self.root = Node()

    def _walk(self, path: str) -> Node:
        node = self.root
        if path == "/":
            return node

        for part in path.split("/")[1:]:
            node = node.children.setdefault(part, Node())
        return node

    def ls(self, path: str) -> list[str]:
        node = self._walk(path)
        if node.is_file:
            return [path.split("/")[-1]]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._walk(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._walk(filePath)
        node.is_file = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        return self._walk(filePath).content
```

## Complexity

- Time: proportional to path length per operation
- Space: proportional to stored directory and file nodes

## Historical Connection

This sits in the same family as:

- `Time Based Key-Value Store`
- `Basic Calculator II`
- `Insert into a Sorted Circular Linked List`

The throughline is mutable state with careful behavior across repeated operations.
