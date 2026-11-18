import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch
from input_helpers import get_positive_float, get_positive_int, get_non_negative_int


def run_helper(helper, entries: list[str]) -> tuple:
    output = io.StringIO()
    with patch("builtins.input", side_effect=entries), redirect_stdout(output):
        result = helper("Enter: ")
    return result, output.getvalue().strip().splitlines()


class TestGetPositiveFloat(unittest.TestCase):
    def test_abc_then_minus_five_then_valid_price(self) -> None:
        result, lines = run_helper(get_positive_float, ["abc", "-5", "12.50"])
        self.assertEqual(result, 12.5)
        self.assertEqual(lines, ["Please enter a valid number, e.g. 12.50",
                                 "Please enter a number greater than zero."])

    def test_zero_is_rejected(self) -> None:
        result, lines = run_helper(get_positive_float, ["0", "3"])
        self.assertEqual(result, 3.0)
        self.assertEqual(lines, ["Please enter a number greater than zero."])

    def test_valid_first_entry_prints_nothing(self) -> None:
        result, lines = run_helper(get_positive_float, ["7.25"])
        self.assertEqual(result, 7.25)
        self.assertEqual(lines, [])


class TestGetPositiveInt(unittest.TestCase):
    def test_rejects_text_decimals_and_zero(self) -> None:
        result, lines = run_helper(get_positive_int, ["ten", "2.5", "0", "4"])
        self.assertEqual(result, 4)
        self.assertEqual(len(lines), 3)


class TestGetNonNegativeInt(unittest.TestCase):
    def test_zero_is_allowed(self) -> None:
        result, lines = run_helper(get_non_negative_int, ["0"])
        self.assertEqual(result, 0)
        self.assertEqual(lines, [])

    def test_negative_is_rejected_then_valid_accepted(self) -> None:
        result, lines = run_helper(get_non_negative_int, ["-1", "8"])
        self.assertEqual(result, 8)
        self.assertEqual(lines, ["Please enter zero or a positive whole number."])


if __name__ == "__main__":
    unittest.main()
