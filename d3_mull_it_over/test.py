import unittest
from pathlib import Path
from .main import parse_input, process, process_with_disabled_instructions


class TestFunctions(unittest.TestCase):
    PARSED_INPUT = []
    INPUT_FILE = Path(__file__).parent / "test_input.txt"

    PARSED_INPUT = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    def test_parse_input(self):
        with open(self.INPUT_FILE, "r") as test_input:
            result = parse_input(test_input)

        self.assertEqual(result, self.PARSED_INPUT)

    def test_process(self):
        result = process(self.PARSED_INPUT)        
        assert result == 161

    def test_process_with_disabled_instructions(self):
        data = "mul(1,1)sdfsdfdon't()do_not mul(100,1)do()mul(1,1)don't()do()mul(1,1)don't()mul(1,1)"

        result = process_with_disabled_instructions(data)        
        assert result == 3

    def test_process_with_disabled_instructions_none_disabled(self):
        result = process_with_disabled_instructions(self.PARSED_INPUT)        
        assert result == 161

    def test_process_with_disabled_instructions_all_disabled(self):
        data = "don't()mul(1,1)do()don't()mul(1,1)do()don't()mul(1,1)do()don't()mul(1,1)do()"

        result = process_with_disabled_instructions(data)        
        assert result == 0

    def test_process_with_disabled_instructions_final_disabled(self):
        data = "mul(1,1)don't()mul(1,1)"

        result = process_with_disabled_instructions(data)        
        assert result == 1

    def test_process_with_disabled_instructions_nested_dont(self):
        data = "mul(7,1)don't()mul(100,1)don't()mul(100,1)do()do()mul(1,7)"

        result = process_with_disabled_instructions(data)
        print(result)
        assert result == 14


if __name__ == "__main__":
    unittest.main()
