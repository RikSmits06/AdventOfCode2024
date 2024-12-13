import re
import math


class ClawMachine:

    diffA = None
    diffB = None
    prize = None

    def __init__(self, diffA, diffB, prize):
        self.diffA = diffA
        self.diffB = diffB
        self.prize = prize

    def solve(self):
        # [(w, v)]
        solutionsX = []
        equalSolutions = []
        iterMaxX1 = min(100, math.ceil(self.prize[0] / self.diffA[0]))
        iterMaxX2 = min(100, math.ceil(self.prize[0] / self.diffB[0]))
        w = 0
        while w <= iterMaxX1:
            v = 0
            while v <= iterMaxX2:
                ans = eval(f"{w}*{self.diffA[0]}+{v}*{self.diffB[0]}=={self.prize[0]}")
                if ans:
                    solutionsX.append((w, v))
                v += 1
            w += 1
        for w, v in solutionsX:
            ans = eval(f"{w}*{self.diffA[1]}+{v}*{self.diffB[1]}=={self.prize[1]}")
            if ans:
                equalSolutions.append((w, v))

        if len(equalSolutions) == 0:
            return 0

        lowest = equalSolutions[0]
        costs = equalSolutions[0][0] * 3 + equalSolutions[0][1]
        for sol in equalSolutions:
            c = sol[0] * 3 + sol[1]
            if c < costs:
                costs = c
                lowest = sol

        # print(f"Lowest={lowest}, costs={costs}")
        return costs

    def __repr__(self):
        return f"A: {self.diffA}, B: {self.diffB}, PRIZE: {self.prize}"


contents = open("input.txt", "r").read()
contents = contents.replace("Button A: X+", " ")
contents = contents.replace(", Y+", " ")
contents = contents.replace("Button B: X+", " ")
contents = contents.replace("Prize: X=", " ")
contents = contents.replace(", Y=", " ")

numbers = contents.split()
machines: list[ClawMachine] = []

while len(numbers) > 0:
    machines.append(
        ClawMachine(
            (int(numbers.pop(0)), int(numbers.pop(0))),
            (int(numbers.pop(0)), int(numbers.pop(0))),
            (int(numbers.pop(0)), int(numbers.pop(0))),
        )
    )

total = 0
for machine in machines:
    total += machine.solve()
print(total)
