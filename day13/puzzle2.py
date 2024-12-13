import z3


class ClawMachineV2:

    Ax = None
    Bx = None
    Ay = None
    By = None
    Px = None
    Py = None
    g = 10000000000000

    def __init__(self, diffA, diffB, prize):
        self.diffA = diffA
        self.diffB = diffB
        self.prize = prize
        self.Ax, self.Ay = diffA
        self.Bx, self.By = diffB
        self.Px, self.Py = prize

    def solve(self):
        s = z3.Optimize()
        v = z3.Int("v")
        w = z3.Int("w")
        s.add(self.Px + self.g == w * self.Ax + v * self.Bx)
        s.add(self.Py + self.g == w * self.Ay + v * self.By)
        s.minimize(3 * w + v)
        if s.check() == z3.sat:
            return s.model().eval(3 * w + v).as_long()
        return 0

    def __repr__(self):
        return f"A: {self.diffA}, B: {self.diffB}, PRIZE: {self.prize}"


contents = open("input.txt", "r").read()
contents = contents.replace("Button A: X+", " ")
contents = contents.replace(", Y+", " ")
contents = contents.replace("Button B: X+", " ")
contents = contents.replace("Prize: X=", " ")
contents = contents.replace(", Y=", " ")

numbers = contents.split()
machines: list[ClawMachineV2] = []

while len(numbers) > 0:
    machines.append(
        ClawMachineV2(
            (int(numbers.pop(0)), int(numbers.pop(0))),
            (int(numbers.pop(0)), int(numbers.pop(0))),
            (
                int(numbers.pop(0)),
                int(numbers.pop(0)),
            ),
        )
    )

total = 0
for machine in machines:
    total += machine.solve()
    print("Solved...")
print(total)
