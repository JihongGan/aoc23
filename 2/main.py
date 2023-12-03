# advent of code 2023 day 2
import re

INPUT = "2/input.txt"
R, G, B = 12, 13, 14

def sum_possible_IDs() -> int:
    with open(INPUT, "r") as f:
        lines = f.readlines()
        s = 0
        for line in lines:
            Id, max_r, max_g, max_b = process_line(line)
            if max_r <= R and max_g <= G and max_b <= B:
                s += Id
        return s

def process_line(line: str) -> (int, int, int, int):
    """Given a game line, returns (Id, max_r, max_g, max_b)."""
    pattern = r"Game (\d+):((?: \d+ (?:red|green|blue)[,;]?)+)"
    count_pattern = r"(\d+) (red|green|blue)"

    game_id_match = re.match(pattern, line)
    if not game_id_match:
        raise ValueError("Invalid line" + line)
    game_id = int(game_id_match.group(1))

    color_counts = re.findall(count_pattern, game_id_match.group(2))
    max_r, max_g, max_b = 0, 0, 0
    for count, color in color_counts:
        count = int(count)
        if color == "red":
            max_r = max(max_r, count)
        elif color == "green":
            max_g = max(max_g, count)
        elif color == "blue":
            max_b = max(max_b, count)

    return game_id, max_r, max_g, max_b

def sum_powers() -> int:
    with open(INPUT, "r") as f:
        lines = f.readlines()
        s = 0
        for line in lines:
            _, max_r, max_g, max_b = process_line(line)
            s += max_r * max_g * max_b
        return s

if __name__ == "__main__":
    print("Pt. 1 ans: " + str(sum_possible_IDs()))
    print("Pt. 2 ans: " + str(sum_powers()))
