# word_bitmask

A small Python experiment: compare two ways to check whether two words (assumed to be lowercase `[a-z]`) share at least one letter.

- **SetWordComparator**: uses `set(...).isdisjoint(...)`
- **BitwiseWordComparator**: encodes each word as a 26-bit mask (one bit per letter) and tests overlap with `mask1 & mask2 != 0`  
  (final version includes an `lru_cache` for the encoding step)

## Benchmark (500,000 random pairs)
- **BitwiseWordComparator**: ~299 ms total, ~599 ns/pair
- **SetWordComparator**: ~329 ms total, ~659 ns/pair

Both implementations return the same results on the same inputs.

## Takeaway
In pure Python, interpreter overhead dominates quickly: switching to a bitmask approach does not automatically yield massive speedups. The goal here is to evaluate an algorithmic representation change while keeping the code maximally clear.
