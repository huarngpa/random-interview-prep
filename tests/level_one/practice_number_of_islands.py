import unittest

from interview_prep.harness import Case, assert_cases
from problems.level_one.number_of_islands import solve


class NumberOfIslandsPracticeTests(unittest.TestCase):
    def test_cases(self) -> None:
        cases = [
            Case(
                name="one large island",
                args=(
                    [
                        ["1", "1", "1", "1", "0"],
                        ["1", "1", "0", "1", "0"],
                        ["1", "1", "0", "0", "0"],
                        ["0", "0", "0", "0", "0"],
                    ],
                ),
                expected=1,
            ),
            Case(
                name="three islands",
                args=(
                    [
                        ["1", "1", "0", "0", "0"],
                        ["1", "1", "0", "0", "0"],
                        ["0", "0", "1", "0", "0"],
                        ["0", "0", "0", "1", "1"],
                    ],
                ),
                expected=3,
            ),
            Case(name="all water", args=([["0", "0"], ["0", "0"]],), expected=0),
            Case(name="single land cell", args=([["1"]],), expected=1),
        ]

        assert_cases(solve, cases)


if __name__ == "__main__":
    unittest.main()
