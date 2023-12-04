# advent of code 2023 day 4 pt 2
import re

INPUT = "4/input.txt"

class Solution:
    def __init__(self) -> None:
        self.matches = []
        self.cards = 0
        with open(INPUT, "r") as f:
            for line in f:
                if line == "\n":
                    continue
                self.cards += 1
                _, line = line.strip().split(":")
                winning, hand = line.split("|")
                winning = [int(num) for num in re.findall(r"\d+", winning)]
                hand = [int(num) for num in re.findall(r"\d+", hand)]
                self.matches.append(len(set(winning) & set(hand)))
        self.winnables = [1 for _ in range(self.cards)]

    def get_winnables(self) -> None:
        for i in range(self.cards-1, -1, -1):
            self.winnables[i] += sum(self.winnables[j] for j in range(i+1, min(i+self.matches[i]+1, self.cards)))

    def total_cards(self) -> int:
        self.get_winnables()
        return sum(self.winnables)

if __name__ == "__main__":
    sol = Solution()
    print("Pt. 2 ans: " + str(sol.total_cards()))
