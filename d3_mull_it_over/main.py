from argparse import ArgumentParser
from pathlib import Path
from typing import Iterator
import re

MUL_REGEX = r"mul\((?P<left>\d{1,3})\,(?P<right>\d{1,3})\)"
DISABLED_REGEX = r"(don\'t\(\).*?)+do\(\)"

def parse_input(input_file) -> Iterator[list[int]]:
    return input_file.read()


def process(data):
    # extract all pairs of numbers in the enabled instructions
    pairs = [(int(m.group("left")), int(m.group("right"))) for m in re.finditer(MUL_REGEX, data)]

    return sum([x * y for x, y in pairs])

def process_with_disabled_instructions(data):
    """
    The general strategy is to only find stretches of enabled instructions.

    We do this through elimination:
        1. Find all stretches of don't()...do() and remove them
        2. If there is a final don't() instruction that does not have a corresponding do() instruction, 
            then remove from that don't() instruction to the end of the string
    After we have only the enabled instructions, we can extract the pairs of numbers and multiply them
    Instructions are enabled by default

    """

    enabled_spans = []
    start = 0

    # Find all stretches of don't()...do() and remove them
    for m in re.finditer(DISABLED_REGEX, data, flags=re.DOTALL):
        enabled_spans.append((start, m.start()))
        start = m.end()
    else:
        # We still need to handle the last stretch of instructions after the last do()
        # If this final span contains an unmatched don't() instruction then remove that stretch
        # as well, else add the whole stretch to the enabled instructions
        if (final_disable_pos := data[start:len(data)].find("don't()")) != -1:
            enabled_spans.append((start, start + final_disable_pos))
        else:
            enabled_spans.append((start, len(data)))

    enabled_instruction = "".join(data[start:end] for start, end in enabled_spans)
    
    # extract all pairs of numbers in the enabled instructions
    pairs = [(int(m.group("left")), int(m.group("right"))) for m in re.finditer(MUL_REGEX, enabled_instruction)]

    return sum([x * y for x, y in pairs])


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
    print("Result: ", process_with_disabled_instructions(data))
