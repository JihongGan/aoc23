# advent of code 2023 day 4 pt 1
import re

INPUT = "4/input.txt"

def get_card_points(winning: list, hand: list) -> int:
    points = 0
    for num in hand:
        if num in winning:
            points = 1 if points == 0 else points * 2
    return points

def get_total_points() -> int:
    total = 0

    with open(INPUT, "r") as f:
        for line in f:
            _, line = line.strip().split(":")
            winning, hand = line.split("|")

            winning = re.findall(r"\d+", winning)
            hand = re.findall(r"\d+", hand)

            winning = [int(num) for num in winning]
            hand = [int(num) for num in hand]

            total += get_card_points(winning, hand)

    return total

if __name__ == "__main__":
    print("Pt. 1 ans: " + str(get_total_points()))
