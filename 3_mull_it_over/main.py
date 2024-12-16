from argparse import ArgumentParser
from pathlib import Path
from typing import Iterator
import re

INSTR_REGEX = re.compile(r"mul\((\d{1,3})\,(\d{1,3})\)")
DO_REGEX = re.compile(r"do(?!n\'t)")
DONT_REGEX = re.compile(r"don\'t")

def parse_input(input_file) -> Iterator[list[int]]:
    return input_file.read()


def process(data):
    pairs = [(int(m.group(1)), int(m.group(2))) for m in INSTR_REGEX.finditer(data)]
    return sum(a * b for a, b in pairs)


def process_with_instructions(data):
    dos = [m.start() for m in DO_REGEX.finditer(data)]
    donts = [m.start() for m in DONT_REGEX.finditer(data)]
    print(dos)
    print(donts)

    pairs = [(int(m.group(1)), int(m.group(2))) for m in INSTR_REGEX.finditer(data)]
    for pair in pairs:
        pass

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("filename", nargs="?", default="input.txt")
    args = parser.parse_args()

    with open(Path(__file__).parent / args.filename, "r") as input_file:
        data = parse_input(input_file)

    print("Part 1")
    print("------")
    print("Result: ", process(data))

    print("\nPart 2")
    print("------")
    print("Result: ", process_with_instructions(data))
