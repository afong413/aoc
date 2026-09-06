from pathlib import Path
from typing import Literal, overload

from tqdm.auto import tqdm

import __main__


def input() -> str:
    path = Path(__main__.__file__).parent / 'input.txt'
    return path.read_text().strip()


@overload
def lines(bar: Literal[False]) -> list[str]: ...
@overload
def lines(bar: Literal[True]) -> tqdm[str]: ...
@overload
def lines() -> tqdm[str]: ...
def lines(bar: bool = True) -> list[str] | tqdm[str]:
    l = input().split('\n')
    if bar:
        return tqdm(input().split('\n'))
    return l
