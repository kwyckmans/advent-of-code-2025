from enum import Enum

from utils import run_day


class Direction(Enum):
    LEFT = "L"
    RIGHT = "R"


def parse_input(lines: list[str]) -> list[tuple[Direction, int]]:
    return [(Direction(line[:1]), int(line[1:])) for line in lines]


def part1(data: list[tuple[Direction, int]]) -> int:
    result = count_zero(data)
    return result[0]


def part2(data: list[tuple[Direction, int]]) -> int:
    result = count_zero(data)
    return result[1]


def count_zero(data: list[tuple[Direction, int]]) -> tuple[int, int]:
    dial = 50
    num_zero = 0
    num_passed_zero = 0

    for direction, distance in data:
        # 0, 1, 2
        num_passed_zero += distance // 100
        distance = distance - (distance // 100) * 100

        match direction:
            case Direction.LEFT:
                result = (dial - distance) % 100

                if result != 0 and dial != 0 and result >= dial:
                    num_passed_zero += 1
            case Direction.RIGHT:
                result = (dial + distance) % 100

                if result != 0 and dial != 0 and result <= dial:
                    num_passed_zero += 1

        if result == 0:
            num_zero += 1

        print(f"Moved from {dial} to {result}")
        dial = result

    return num_zero, num_zero + num_passed_zero


if __name__ == "__main__":
    run_day(1, parse_input, part1, part2)
