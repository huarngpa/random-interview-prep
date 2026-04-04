# Web Crawler Multithreaded

- LeetCode: [1242. Web Crawler Multithreaded](https://leetcode.com/problems/web-crawler-multithreaded/)
- Category: `Public-signal closest match`
- Why it is here: public reports repeatedly mention crawler tasks with concurrency or multithreading follow-ups.

## Framework Classification

- Input structure: implicit graph of URLs plus concurrent workers
- Output asks for the reachable same-host URL set
- Repeated operation: schedule crawl work while preserving deduplication
- Remembered state: shared visited set and work queue

## Pattern Choice

- Primary: graph traversal plus concurrency control
- Secondary: thread-safe shared state

## Invariant

Every URL is processed at most once even though multiple workers run concurrently.

## Skeleton Plan

1. Keep a shared queue of URLs to crawl.
2. Protect the shared `visited` set with a lock.
3. Spawn worker threads that pop, fetch, filter, and enqueue.
4. Wait for all workers to finish.

## Python Solution

```python
from queue import Queue
from threading import Lock, Thread


class Solution:
    def crawl(self, startUrl: str, htmlParser: "HtmlParser") -> list[str]:
        host = startUrl.split("/")[2]
        seen = {startUrl}
        seen_lock = Lock()
        queue = Queue()
        queue.put(startUrl)

        def worker() -> None:
            while True:
                url = queue.get()
                if url is None:
                    queue.task_done()
                    return

                for next_url in htmlParser.getUrls(url):
                    if next_url.split("/")[2] != host:
                        continue

                    with seen_lock:
                        if next_url in seen:
                            continue
                        seen.add(next_url)

                    queue.put(next_url)

                queue.task_done()

        workers = [Thread(target=worker) for _ in range(8)]
        for thread in workers:
            thread.start()

        queue.join()

        for _ in workers:
            queue.put(None)
        for thread in workers:
            thread.join()

        return list(seen)
```

## Common Pitfalls

- Using a shared `set` without synchronization
- Marking visited too late and enqueuing duplicate work
- Forgetting worker shutdown logic

## Related Docs

- [Algorithm Framework](../algorithm-framework.md)
