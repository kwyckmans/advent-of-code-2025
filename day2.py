from utils import parse_separated, run_day


def parse_input(lines: list[str]) -> list[tuple[int, int]]:
    items = parse_separated(lines)
    ranges = []
    for item in items:
        start, end = item.split("-")
        ranges.append((int(start), int(end)))
    print(f"Parsed {len(ranges)} ranges:")
    print(ranges[:5], "..." if len(ranges) > 5 else "")
    return ranges


def part1(data: list[tuple[int, int]]) -> int:
    for start, end in data:
        for i in range(start, end + 1):
            s = str(i)
            is_even = len(s) % 2 == 0
            print(f"{i}: len={len(s)}, even={is_even}")
    return 0


def part2(data: list[tuple[int, int]]) -> int:
    # TODO: Implement part 2
    return 0


if __name__ == "__main__":
    run_day(2, parse_input, part1, part2)
