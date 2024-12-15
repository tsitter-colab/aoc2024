import unittest
from main import parse_input, total_distance, similarity


class TestFunctions(unittest.TestCase):
    PARSED_INPUT = ([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9])
    INPUT_FILE = "test_input.txt"

    def test_parse_input(self):
        with open(self.INPUT_FILE, "r") as test_input:
            result = parse_input(test_input)

        self.assertEqual(result, self.PARSED_INPUT)

    def test_total_distance(self):
        result = total_distance(*self.PARSED_INPUT)
        self.assertEqual(result, 11)

    def test_similarity(self):
        result = similarity(*self.PARSED_INPUT)

        self.assertEqual(result, 31)


if __name__ == "__main__":
    unittest.main()
