from collections.abc import Generator
from enum import Enum
from pathlib import Path


class Direction(Enum):
    LEFT = "L"
    RIGHT = "R"


def main() -> None:
    test_input = Path("inputs/day1.txt")
    parsed_input = [(Direction(line[:1]), int(line[1:])) for line in parse(test_input)]
    print(parsed_input)
    print(count_zero(parsed_input))


def count_zero(data: list[tuple[Direction, int]]) -> int:
    dial = 50
    num_zero = 0
    num_passed_zero = 0

    for direction, distance in data:
        # 0, 1, 2
        num_passed_zero += (distance // 100)
        distance = distance - (distance // 100) * 100

        match direction:
            case Direction.LEFT:
                result = (dial - distance) % 100
                print(f"Moved from {dial} to {result}")

                if result != 0 and dial != 0 and result >= dial:
                    print("passed 0")
                    num_passed_zero += 1
            case Direction.RIGHT:
                result = (dial + distance) % 100
                print(f"Moved from {dial} to {result}")

                if result != 0 and dial != 0 and result <= dial:
                    print("passed 0")
                    num_passed_zero += 1

        if result == 0:
            num_zero += 1

        dial = result

    return num_zero, num_zero + num_passed_zero


def parse(path: Path) -> Generator[str, None, None]:
    with open(path) as f:
        for line in f:
            yield line.strip()


if __name__ == "__main__":
    print(1//100)
    print(101//100)
    print(201//100)
    main()
