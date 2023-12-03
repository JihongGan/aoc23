# advent of code 2023 day 1
from typing import Callable, Iterable

INPUT = "input.txt"

def sum_calibration_values() -> int:
    with open(INPUT, "r") as f:
        lines = f.readlines()
        sum = 0
        for line in lines:
            sum += decode_line(line)
        return sum
    
def first_digit(s: str, func: Callable[[Iterable], Iterable]) -> str:
    for c in func(s):
        if c.isdigit():
            return c
    raise ValueError("No digit found in string")

def decode_line(line: str) -> int:
    digits_spelled = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", 
                      "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    first, last = "", ""

    for i, c in enumerate(line):
        cur = ""
        if c.isdigit():
            cur = c
        elif c.isalpha():
            for s in range(3, 6):
                w = line[i:i+s]
                if w in digits_spelled:
                    cur = digits_spelled[w]
                    break
        
        if cur:
            if not first:
                first = cur
            last = cur
    
    if not first or not last:
        raise ValueError("No digit found in line" + line)
    return int(first + last)
        
if __name__ == "__main__":
    print(sum_calibration_values())
