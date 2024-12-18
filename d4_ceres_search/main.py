from argparse import ArgumentParser
from pathlib import Path
from typing import Iterator


def parse_input(input_file) -> Iterator[list[int]]:
    for line in input_file:
        yield line


def process(data):
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
    print("Result: ", process(data))
