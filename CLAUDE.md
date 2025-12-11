# CLAUDE.md

Guidance for Claude Code when working with this Advent of Code 2025 repository.

## Development Setup

Python 3.12 with `uv` for dependency management. Virtual environment: `.venv/`.

**Always use `uv` commands for running code and managing dependencies.**

```bash
# Run code
uv run day1.py

# Manage dependencies
uv add <package>
uv sync
```

## Project Structure

- `day1.py`, `day2.py`, etc. - Daily solutions (no leading zeros)
- `utils.py` - Shared utility functions
- `inputs/` - Puzzle inputs (gitignored)
- `.python-version` - Python 3.12

## Code Quality Standards

- Always add type hints
- After every change: lint and format with `uv run ruff check` and `uv run ruff format`
- Verify types with `uv run pyright`

## Solution Patterns

- Store inputs in `inputs/dayN.txt`
- Each puzzle has two parts that build on each other
- Parse input first, then solve the logic
- Write idiomatic python code.

## Solution Template

Each day file should follow this pattern:

```python
from utils import run_day

def parse_input(lines: list[str]) -> YourDataType:
    # Transform raw lines into structured data
    return parsed_data

def part1(data: YourDataType) -> int:
    # Solve part 1
    return result

def part2(data: YourDataType) -> int:
    # Solve part 2
    return result

if __name__ == "__main__":
    run_day(DAY_NUMBER, parse_input, part1, part2)
```

Run with: `uv run dayN.py` or `uv run dayN.py --test`