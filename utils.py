import argparse
from collections.abc import Callable, Generator
from pathlib import Path
from typing import TypeVar

T = TypeVar("T")


def parse(path: Path) -> Generator[str, None, None]:
    with open(path) as f:
        for line in f:
            yield line.strip()


def get_input_path(day: int, test: bool = False) -> Path:
    """Construct input file path for a given day."""
    suffix = "_test" if test else ""
    return Path(f"inputs/day{day}{suffix}.txt")


def read_input(day: int, test: bool = False) -> list[str]:
    """Read input file and return as list of stripped lines."""
    return list(parse(get_input_path(day, test)))


def parse_separated(lines: list[str], separator: str = ",") -> list[str]:
    """
    Parse separated values from lines into a flat list.

    Joins all lines and splits by separator, returning non-empty stripped values.

    Args:
        lines: Input lines
        separator: Separator character (default: comma)

    Returns:
        List of stripped non-empty values

    Example:
        >>> parse_separated(["1,2,3", "4,5"])
        ["1", "2", "3", "4", "5"]
    """
    joined = separator.join(lines)
    return [item.strip() for item in joined.split(separator) if item.strip()]


def run_day(
    day: int,
    parse_func: Callable[[list[str]], T],
    part1: Callable[[T], int],
    part2: Callable[[T], int] | None = None,
) -> None:
    """
    Run a day's solution with argparse handling.

    Args:
        day: Day number
        parse_func: Function to transform raw lines into structured data
        part1: Solver for part 1
        part2: Optional solver for part 2
    """
    parser = argparse.ArgumentParser(description=f"Advent of Code Day {day}")
    parser.add_argument("--test", action="store_true", help="Use test input")
    args = parser.parse_args()

    lines = read_input(day, args.test)
    data = parse_func(lines)

    result1 = part1(data)
    print(f"Part 1: {result1}")

    if part2:
        result2 = part2(data)
        print(f"Part 2: {result2}")
