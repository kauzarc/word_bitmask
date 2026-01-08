from unittest import TestCase, main

from comparators import WordComparator, SetWordComparator, BitwiseWordComparator


class TestWordComparator(TestCase):
    comparators: list[WordComparator] = [SetWordComparator(), BitwiseWordComparator()]

    def test_on_examples(self) -> None:
        examples: list[tuple[str, str, bool]] = [
            ("abc", "def", False),
            ("abc", "xa", True),
            ("hello", "world", True),
            ("aaaa", "b", False),
            ("xyz", "y", True),
        ]

        for comparator in self.comparators:
            for word1, word2, expected in examples:
                self.assertEqual(comparator.share_letter(word1, word2), expected)


if __name__ == "__main__":
    main()
