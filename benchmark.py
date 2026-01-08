from dataclasses import dataclass
from typing import Sequence, Iterator
from random import Random
from time import perf_counter_ns

from comparators import WordComparator


@dataclass(frozen=True)
class BenchmarkResult:
    name: str
    duration: float
    n_pairs: int
    n_true: int

    def __str__(self) -> str:
        true_pct: float = (self.n_true / self.n_pairs) * 100 if self.n_pairs else 0
        ns_per_pair: float = self.duration / self.n_pairs

        return (
            f"┏━ Benchmark ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"┃ Comparator : {self.name}\n"
            f"┃ Time       : {self.duration:.6f} ns\n"
            f"┃ Pairs      : {self.n_pairs:,}\n"
            f"┃ True       : {self.n_true:,}  ({true_pct:.2f}%)\n"
            f"┃ Cost       : {ns_per_pair:,.1f} ns / pair\n"
            f"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )


class WordComparatorBenchmark:
    def __init__(
        self,
        comparator: WordComparator,
        words: Sequence[str],
        n_pairs: int,
        seed: int = 0,
    ):
        self.comparator = comparator
        self.words = words
        self.n_pairs = n_pairs
        self.rng = Random(seed)

    def run(self) -> BenchmarkResult:
        t0: int = perf_counter_ns()

        n_true: int = sum(
            self.comparator.share_letter(word1, word2)
            for word1, word2 in self._pairs_generator()
        )

        t1: int = perf_counter_ns()

        return BenchmarkResult(
            name=type(self.comparator).__name__,
            duration=t1 - t0,
            n_pairs=self.n_pairs,
            n_true=n_true,
        )

    def _pairs_generator(self) -> Iterator[tuple[str, str]]:
        for _ in range(self.n_pairs):
            yield self._get_word(), self._get_word()

    def _get_word(self) -> str:
        return self.rng.choice(self.words)
