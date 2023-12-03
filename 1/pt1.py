# advent of code 2023 day 1
from typing import Callable, Iterable

INPUT = "1/input.txt"

def sum_calibration_values() -> int:
    with open(INPUT, "r") as f:
        lines = f.readlines()
        sum = 0
        for line in lines:
            sum += int(first_digit(line, lambda x: x) + first_digit(line, reversed))
        return sum
    
def first_digit(s: str, func: Callable[[Iterable], Iterable]) -> str:
    for c in func(s):
        if c.isdigit():
            return c
    raise ValueError("No digit found in string")
        
if __name__ == "__main__":
    print(sum_calibration_values())
