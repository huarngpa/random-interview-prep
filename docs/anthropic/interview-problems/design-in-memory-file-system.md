# Design In-Memory File System

- LeetCode: [588. Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/)
- Category: `Public-signal closest match`
- Why it is here: public Anthropic anecdotes mention progressive in-memory system design more than pure puzzle solving.

## Framework Classification

- Input structure: hierarchical mutable state
- Output asks for correct behavior across multiple operations
- Repeated operation: walk and update path-based structure
- Remembered state: trie-like tree of directories and files

## Pattern Choice

- Primary: trie/tree-backed stateful object design
- Secondary: careful API behavior and edge cases

## Invariant

Each node always represents exactly one path segment, and file content lives only on file nodes.

## Skeleton Plan

1. Represent directories and files as nodes.
2. Walk paths by splitting on `/`.
3. Create missing directory nodes for `mkdir` or file paths.
4. Keep children sorted only at read time.

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

## Common Pitfalls

- Mixing file nodes and directory nodes
- Sorting children on every write instead of on `ls`
- Mishandling the root path `/`

## Related Docs

- [Algorithm Framework](../algorithm-framework.md)
