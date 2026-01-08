from comparators import SetWordComparator, BitwiseWordComparator
from benchmark import WordComparatorBenchmark

WORDS = [
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

N_PAIRS = 500_000
SEED = 42


def main() -> None:
    results = [
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
