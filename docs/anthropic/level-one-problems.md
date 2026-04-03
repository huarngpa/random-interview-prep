# Level One Problems

This is the first practice set.

The goal is not to grind random easies. The goal is to learn one clean recognition pattern at a time.

## The Set

### 1. Two Sum

- Pattern: hash map
- File: `problems/level_one/two_sum.py`
- Test: `tests/level_one/practice_two_sum.py`
- Run:

```bash
uv run python -m unittest tests.level_one.practice_two_sum -v
```

### 2. Valid Anagram

- Pattern: counting with hash map or `Counter`
- File: `problems/level_one/valid_anagram.py`
- Test: `tests/level_one/practice_valid_anagram.py`
- Run:

```bash
uv run python -m unittest tests.level_one.practice_valid_anagram -v
```

### 3. Binary Search

- Pattern: binary search on sorted input
- File: `problems/level_one/binary_search.py`
- Test: `tests/level_one/practice_binary_search.py`
- Run:

```bash
uv run python -m unittest tests.level_one.practice_binary_search -v
```

### 4. Best Time To Buy And Sell Stock

- Pattern: one-pass scan / two pointers
- File: `problems/level_one/best_time_to_buy_and_sell_stock.py`
- Test: `tests/level_one/practice_best_time_to_buy_and_sell_stock.py`
- Run:

```bash
uv run python -m unittest tests.level_one.practice_best_time_to_buy_and_sell_stock -v
```

### 5. Longest Substring Without Repeating Characters

- Pattern: sliding window
- File: `problems/level_one/longest_substring_without_repeating_characters.py`
- Test: `tests/level_one/practice_longest_substring_without_repeating_characters.py`
- Run:

```bash
uv run python -m unittest tests.level_one.practice_longest_substring_without_repeating_characters -v
```

### 6. Number Of Islands

- Pattern: DFS or BFS on a grid
- File: `problems/level_one/number_of_islands.py`
- Test: `tests/level_one/practice_number_of_islands.py`
- Run:

```bash
uv run python -m unittest tests.level_one.practice_number_of_islands -v
```

## Recommended Order

1. Two Sum
2. Valid Anagram
3. Binary Search
4. Best Time To Buy And Sell Stock
5. Longest Substring Without Repeating Characters
6. Number Of Islands

## Why These Six?

They give you one clean representative for six high-value patterns:

- hash map lookup
- frequency counting
- binary search
- one-pass state tracking
- sliding window
- graph traversal

If these feel comfortable, level two should move into:

- prefix sum
- intervals
- heap
- topological sort
- union find
- memoization / DP
