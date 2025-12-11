# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Advent of Code 2025 project using Python 3.12 and uv for dependency management. The project is structured to solve daily coding challenges from adventofcode.com.

## Development Setup

This project uses `uv` as the package manager (a fast Python package installer and resolver). The virtual environment is managed in `.venv/`.

**IMPORTANT: Always use `uv` commands for running Python code and managing dependencies.**

### Running Code

```bash
# Run Python files
uv run main.py
uv run <script>.py
```

### Managing Dependencies

```bash
# Add a dependency
uv add <package-name>

# Install/sync dependencies
uv sync

# Lock dependencies
uv lock
```

## Project Structure

- `main.py` - Entry point for the application
- `input/` - Directory for puzzle inputs (gitignored)
- `.python-version` - Specifies Python 3.12

## Advent of Code Patterns

When implementing daily solutions:
- Puzzle inputs are typically stored in the `input/` directory (gitignored)
- Each day's solution is usually organized by day number (e.g., `day01.py`, `day02.py`)
- Solutions typically have two parts that build on each other
- Input parsing is often the first step before solving the puzzle logic
- Always add type hints.
- after every chane, lint and format with ruff
- Use pyright to check type hints