from argparse import ArgumentParser
from collections import Counter
from pathlib import Path


def parse_input(input_file) -> tuple[list[int], list[int]]:
    # Reads the input and returns two lists (left column, right column) as sorted ints
    def number_generator(input_file):
        for line in input_file:
            yield map(int, line.split())

    left_numbers, right_numbers = zip(*number_generator(input_file))

    return sorted(left_numbers), sorted(right_numbers)


def total_distance(l1, l2):
    return sum([abs(a - b) for a, b in zip(l1, l2)])


def similarity(l1, l2):
    # For each number in l1, multiple it by the number of times it appears in l2
    # Then sum the resultspip
    l2_counts = Counter(l2)
    return sum([a * l2_counts[a] for a in l1])


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("filename", nargs="?", default="input.txt")
    args = parser.parse_args()

    with open(Path(__file__).parent / args.filename, "r") as input_file:
        l1, l2 = parse_input(input_file)

    print("Part 1")
    print("------")
    print("Total distance: ", total_distance(l1, l2))

    print("\nPart 2")
    print("------")
    print("Similarity: ", similarity(l1, l2))
