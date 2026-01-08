from typing import Protocol
from functools import reduce
from functools import lru_cache


class WordComparator(Protocol):
    def share_letter(self, word1: str, word2: str) -> bool: ...


class SetWordComparator:
    def share_letter(self, word1: str, word2: str) -> bool:
        return not set(word1).isdisjoint(word2)


FIRST_LETTER_ORD: int = ord("a")
EMPTY_BITSET: int = 0


class BitwiseWordComparator:
    def share_letter(self, word1: str, word2: str) -> bool:
        return (self._encode_word(word1) & self._encode_word(word2)) != 0

    @lru_cache(maxsize=None)
    def _encode_word(self, word: str) -> int:
        return reduce(self._update_bitset, word, EMPTY_BITSET)

    def _update_bitset(self, bitset: int, char: str) -> int:
        bit_idx = ord(char) - FIRST_LETTER_ORD
        return bitset | (1 << bit_idx)
