"""
This is a CLI tool
"""

import sys

from imppkg.harmonic_mean import harmonic_mean
from termcolor import colored


def _parse_nums(inputs: list[str]) -> list[float]:
    try:
        return [float(num) for num in inputs]
    except ValueError:
        return []


def _calculate_result(nums: list[float]) -> float:
    try:
        return harmonic_mean(nums)
    except ZeroDivisionError:
        return 0.0


def _format_output(result: float) -> str:
    return colored(str(result), "red", "on_cyan", attrs=["bold"])


def main() -> None:
    nums = _parse_nums(sys.argv[1:])
    result = _calculate_result(nums)
    print(_format_output(result))
