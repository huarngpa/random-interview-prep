import unittest

from interview_prep.harness import Case, assert_cases
from problems.level_one.valid_anagram import solve


class ValidAnagramPracticeTests(unittest.TestCase):
    def test_cases(self) -> None:
        cases = [
            Case(name="simple anagram", args=("anagram", "nagaram"), expected=True),
            Case(name="different lengths", args=("rat", "car"), expected=False),
            Case(name="same letters different counts", args=("aacc", "ccac"), expected=False),
            Case(name="empty strings", args=("", ""), expected=True),
        ]

        assert_cases(solve, cases)


if __name__ == "__main__":
    unittest.main()
