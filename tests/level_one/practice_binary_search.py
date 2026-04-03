import unittest

from interview_prep.harness import Case, assert_cases
from problems.level_one.binary_search import solve


class BinarySearchPracticeTests(unittest.TestCase):
    def test_cases(self) -> None:
        cases = [
            Case(name="target in middle", args=([-1, 0, 3, 5, 9, 12], 9), expected=4),
            Case(name="target missing", args=([-1, 0, 3, 5, 9, 12], 2), expected=-1),
            Case(name="single item present", args=([5], 5), expected=0),
            Case(name="single item absent", args=([5], 1), expected=-1),
        ]

        assert_cases(solve, cases)


if __name__ == "__main__":
    unittest.main()
