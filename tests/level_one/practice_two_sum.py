import unittest

from interview_prep.harness import Case, assert_cases
from problems.level_one.two_sum import solve


class TwoSumPracticeTests(unittest.TestCase):
    def test_cases(self) -> None:
        cases = [
            Case(name="basic pair", args=([2, 7, 11, 15], 9), expected=[0, 1]),
            Case(name="later pair", args=([3, 2, 4], 6), expected=[1, 2]),
            Case(name="duplicate values", args=([3, 3], 6), expected=[0, 1]),
            Case(
                name="negative numbers",
                args=([-3, 4, 3, 90], 0),
                expected=[0, 2],
            ),
        ]

        assert_cases(solve, cases)


if __name__ == "__main__":
    unittest.main()
