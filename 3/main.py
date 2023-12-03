# advent of code 2023 day 3
INPUT = "3/input.txt"

class Solution:
    def __init__(self):
        self.schematic = []
        with open(INPUT, "r") as f:
            for line in f:
                self.schematic.append(line.strip())
        self.width = len(self.schematic[0])
        self.height = len(self.schematic)

    def get_number_string(self, i: int, j: int) -> str:
        number = ""
        while j < self.width and self.schematic[i][j].isdigit():
            number += self.schematic[i][j]
            j += 1
        return number
    
    def has_symbol(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        for i in range(x1, x2):
            for j in range(y1, y2):
                if i < 0 or j < 0 or i >= self.height or j >= self.width:
                    continue
                if self.schematic[i][j] != "." and not self.schematic[i][j].isdigit():
                    return True
        return False

    def sum_part_number(self):
        s = 0
        for i in range(self.height):
            j = 0
            while j < self.width:
                if self.schematic[i][j].isdigit():
                    number_string = self.get_number_string(i, j)
                    if self.has_symbol(i-1, j-1, i+2, j+len(number_string)+1):
                        s += int(number_string)
                    j += len(number_string)
                else:
                    j += 1
        return s
    
    def get_numbers(self):
        self.numbers = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for i in range(self.height):
            j = 0
            while j < self.width:
                if self.schematic[i][j].isdigit():
                    number_string = self.get_number_string(i, j)
                    for y in range(j, j+len(number_string)):
                        self.numbers[i][y] = int(number_string)
                    j += len(number_string)
                else:
                    j += 1

    def get_adjacent_numbers(self, i: int, j: int) -> list:
        adjacent_numbers = []
        for x in range(i-1, i+2):
            y = j-1
            while y < j+2:
                if x < 0 or y < 0 or x >= self.height or y >= self.width:
                    y += 1
                    continue
                if self.schematic[x][y].isdigit():
                    adjacent_numbers.append(self.numbers[x][y])
                    while y < self.width and self.schematic[x][y].isdigit():
                        y += 1
                else:
                    y += 1
        return adjacent_numbers
    
    def sum_gear_ratios(self):
        self.get_numbers()
        s = 0

        for i in range(self.height):
            for j in range(self.width):
                if self.schematic[i][j] == '*':
                    adjacent_numbers = self.get_adjacent_numbers(i, j)
                    if len(adjacent_numbers) == 2:
                        s += adjacent_numbers[0] * adjacent_numbers[1]

        return s

if __name__ == "__main__":
    sol = Solution()
    # print("Pt. 1 ans: " + sol.sum_part_number())
    print("Pt. 2 ans: " + str(sol.sum_gear_ratios()))
