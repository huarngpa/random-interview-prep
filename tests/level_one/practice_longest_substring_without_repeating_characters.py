import unittest

from interview_prep.harness import Case, assert_cases
from problems.level_one.longest_substring_without_repeating_characters import solve


class LongestSubstringPracticeTests(unittest.TestCase):
    def test_cases(self) -> None:
        cases = [
            Case(name="repeats split window", args=("abcabcbb",), expected=3),
            Case(name="all same", args=("bbbbb",), expected=1),
            Case(name="repeat after gap", args=("pwwkew",), expected=3),
            Case(name="empty string", args=("",), expected=0),
        ]

        assert_cases(solve, cases)


if __name__ == "__main__":
    unittest.main()
