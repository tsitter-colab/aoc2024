import unittest
from pathlib import Path
from .main import parse_input


class TestFunctions(unittest.TestCase):
    PARSED_INPUT = []
    INPUT_FILE = Path(__file__).parent / "test_input.txt"

    def test_parse_input(self):
        with open(self.INPUT_FILE, "r") as test_input:
            result = list(parse_input(test_input))

        self.assertEqual(result, self.PARSED_INPUT)

if __name__ == "__main__":
    unittest.main()
