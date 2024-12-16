import unittest
from .main import is_safe, is_safe_with_dampener, parse_input
from pathlib import Path


class TestFunctions(unittest.TestCase):
    PARSED_INPUT = (
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    )
    INPUT_FILE = Path(__file__).parent / "test_input.txt"

    def test_parse_input(self):
        with open(self.INPUT_FILE, "r") as test_input:
            result = parse_input(test_input)

        self.assertEqual(result, self.PARSED_INPUT)

    def test_is_safe(self):
        expected_results = [True, False, False, False, False, True]

        for i, report in enumerate(self.PARSED_INPUT):
            result = is_safe(report)
            self.assertEqual(result, expected_results[i])

    def test_is_safe_with_dampener(self):
        expected_results = [True, False, False, True, True, True]

        for i, report in enumerate(self.PARSED_INPUT):
            result = is_safe_with_dampener(report)
            self.assertEqual(result, expected_results[i])

    def test_is_safe_with_dampener_final_record(self):
        # Tests that if just the final record is unsafe, the list is still considered safe
        report = [1, 3, 6, 7, 7]
        result = is_safe_with_dampener(report)
        self.assertTrue(result)

    def test_is_safe_with_dampener_final_two_records(self):
        # Tests that if just the final record is unsafe, the list is still considered safe
        report = [1, 3, 6, 7, 7, 7]
        result = is_safe_with_dampener(report)
        self.assertFalse(result)

    def test_only_last_level_bad(self):
        report = [63, 66, 67, 68, 69, 1]
        result = is_safe_with_dampener(report)

        self.assertTrue(result)

    def test_only_first_level_bad(self):
        report = [99, 66, 67, 68, 69, 70]
        result = is_safe_with_dampener(report)

        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
