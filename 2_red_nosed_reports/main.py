from argparse import ArgumentParser
from pathlib import Path
from typing import Iterator


def parse_input(input_file) -> Iterator[list[int]]:
    # Reads the input and returns two lists (left column, right column) as sorted ints

    def number_generator(input_file):
        for line in input_file:
            yield list(map(int, line.split()))

    return tuple(number_generator(input_file))


def is_safe(report) -> bool:
    # Given a list of integers, return True if the list is monotonic (either increasing or decreasing)
    # and all differences between adjacent elements are 1, 2, or 3

    diffs = [b - a for a, b in zip(report, report[1:])]

    if set(diffs) <= {1, 2, 3} or set(diffs) <= {-1, -2, -3}:
        return True

    return False


def is_safe_with_dampener(report) -> bool:
    # Given a list of integers, return True if the list is monotonic (either increasing or decreasing)
    # and all differences between adjacent elements are 1, 2, or 3, except for one element which can be removed
    if is_safe(report):
        return True

    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1 :]):
            return True

    return False


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("filename", nargs="?", default="input.txt")
    args = parser.parse_args()

    with open(Path(__file__).parent / args.filename, "r") as input_file:
        reports = parse_input(input_file)

    print("Part 1")
    print("------")
    print("Total safe: ", sum(is_safe(report) for report in reports))

    print("\nPart 2")
    print("------")
    print(
        "Total safe with dampener: ",
        sum(is_safe_with_dampener(report) for report in reports),
    )
