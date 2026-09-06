from pathlib import Path

import __main__


def input() -> str:
    path = Path(__main__.__file__).parent / 'input.txt'
    return path.read_text()


def lines() -> list[str]:
    return input().split('\n')
