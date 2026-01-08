from comparators import SetWordComparator, BitwiseWordComparator
from benchmark import WordComparatorBenchmark, BenchmarkResult

WORDS: list[str] = [
    "abc",
    "def",
    "ghij",
    "klmno",
    "pqr",
    "stuv",
    "wxyz",
    "aaaa",
    "bbbb",
    "az",
    "za",
    "mnop",
    "qrst",
]

N_PAIRS: int = 500_000
SEED: int = 42


def main() -> None:
    results: list[BenchmarkResult] = [
        benchmark.run()
        for benchmark in (
            WordComparatorBenchmark(comparator, WORDS, N_PAIRS, SEED)
            for comparator in (SetWordComparator(), BitwiseWordComparator())
        )
    ]

    results.sort(key=lambda result: result.duration)

    for result in results:
        print(result)
        print()


if __name__ == "__main__":
    main()
