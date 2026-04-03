import unittest

from interview_prep.harness import Case, assert_cases
from problems.level_one.best_time_to_buy_and_sell_stock import solve


class BestTimeToBuyAndSellStockPracticeTests(unittest.TestCase):
    def test_cases(self) -> None:
        cases = [
            Case(name="basic profit", args=([7, 1, 5, 3, 6, 4],), expected=5),
            Case(name="no profit", args=([7, 6, 4, 3, 1],), expected=0),
            Case(name="profit at end", args=([2, 4, 1],), expected=2),
            Case(name="single day", args=([5],), expected=0),
        ]

        assert_cases(solve, cases)


if __name__ == "__main__":
    unittest.main()
