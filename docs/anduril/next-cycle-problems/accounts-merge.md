# Accounts Merge

- LeetCode: [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)
- Why It Is Likely: this is a realistic next-cycle extension of Anduril's connectivity problems. It combines union find with identity stitching, which is a natural evolution from pure component problems.

## Pattern Family

- union find
- mapping real-world entities to graph connectivity

## Framework Classification

- Input structure: accounts, emails, and ownership labels
- Output asks for merged connected groups
- Repeated operation: union identifiers that belong together
- Hidden structure: emails are nodes, shared-account membership creates edges

## Principle To Internalize

The problem is not really about strings.

It is about connectivity.

The key move is:

- model each email as a node
- union all emails in the same account
- then group by component root

## Solving Walkthrough

1. Create a union-find structure over emails.
2. For each account, union its emails together.
3. Track the owner name for each email.
4. Group all emails by root.
5. Sort each group and prepend the owner name.

## Python Solution

```python
from collections import defaultdict


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x: str) -> str:
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: str, b: str) -> None:
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            self.parent[rb] = ra


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        uf = UnionFind()
        owner = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                owner[email] = name
                uf.union(first_email, email)

        groups = defaultdict(list)
        for email in owner:
            groups[uf.find(email)].append(email)

        answer = []
        for root, emails in groups.items():
            answer.append([owner[root]] + sorted(emails))

        return answer
```

## Complexity

- Time: roughly `O(N alpha(N) + sorting)`
- Space: `O(N)`

## Historical Connection

This extends the historical family of:

- `Number of Islands`
- `Making A Large Island`
- `Number of Distinct Islands`

The new move is mapping messy real-world identifiers into connected components.
