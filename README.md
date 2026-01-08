# word_bitmask

A small Python experiment: compare two ways to check whether two words (assumed to be lowercase `[a-z]`) share at least one letter.

- **SetWordComparator**: uses `set(...).isdisjoint(...)`
- **BitwiseWordComparator**: encodes each word as a 26-bit mask (one bit per letter) and tests overlap with `mask1 & mask2 != 0`  
  (final version includes an `lru_cache` for the encoding step)

## Benchmarks

**Input:** 500,000 random word pairs.

### CPython 3.13.11
- **BitwiseWordComparator**: ~299.5 ms, ~599.0 ns/pair
- **SetWordComparator**: ~329.5 ms, ~658.9 ns/pair

### PyPy 7.3.20 (Python 3.11.13)
- **BitwiseWordComparator**: ~154.3 ms, ~308.6 ns/pair
- **SetWordComparator**: ~166.6 ms, ~333.3 ns/pair


Both implementations return the same results on the same inputs.

## Takeaway
In pure Python, interpreter overhead dominates quickly: switching to a bitmask approach does not automatically yield massive speedups. The goal here is to evaluate an algorithmic representation change while keeping the code maximally clear.
