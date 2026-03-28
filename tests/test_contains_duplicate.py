import unittest

from interview_prep.harness import Case, assert_cases
from problems.contains_duplicate import solve


class ContainsDuplicateTests(unittest.TestCase):
    def test_cases(self) -> None:
        cases = [
            Case(name="empty list", args=([],), expected=False),
            Case(name="all unique", args=([1, 2, 3, 4],), expected=False),
            Case(name="has duplicate", args=([1, 2, 3, 1],), expected=True),
            Case(name="negative numbers", args=([-1, 0, -1],), expected=True),
        ]

        assert_cases(solve, cases)


if __name__ == "__main__":
    unittest.main()
