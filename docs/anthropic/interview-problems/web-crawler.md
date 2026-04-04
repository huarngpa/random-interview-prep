# Web Crawler

- LeetCode: [1236. Web Crawler](https://leetcode.com/problems/web-crawler/)
- Category: `Public-signal closest match`
- Why it is here: public Anthropic interview anecdotes most often mention crawler or scraper style tasks before concurrency follow-ups.

## Framework Classification

- Input structure: implicit graph of URLs
- Output asks for the reachable subset under a hostname constraint
- Repeated operation: fetch neighbors and avoid revisiting states
- Remembered state: visited URLs

## Pattern Choice

- Primary: BFS or DFS on an implicit graph
- Secondary: hostname filtering is a parsing guard, not the main algorithm

## Invariant

Every URL in `visited` has already been discovered from the start host and should never be crawled again.

## Skeleton Plan

1. Extract the host from the starting URL.
2. Traverse URLs reachable from `startUrl`.
3. Only enqueue links from the same host.
4. Use a `visited` set to dedupe.

## Python Solution

```python
from collections import deque


class Solution:
    def crawl(self, startUrl: str, htmlParser: "HtmlParser") -> list[str]:
        host = startUrl.split("/")[2]
        queue = deque([startUrl])
        visited = {startUrl}

        while queue:
            url = queue.popleft()
            for next_url in htmlParser.getUrls(url):
                if next_url in visited:
                    continue
                if next_url.split("/")[2] != host:
                    continue
                visited.add(next_url)
                queue.append(next_url)

        return list(visited)
```

## Common Pitfalls

- Forgetting same-host filtering
- Revisiting URLs and turning the crawl exponential
- Overcomplicating this into shortest path when it is just reachability

## Related Docs

- [Algorithm Framework](../algorithm-framework.md)
