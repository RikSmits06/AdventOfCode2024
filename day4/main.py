import re

contents = open("input.txt", "r").read().split("\n")


def horizontal(lines):
    total = 0
    for line in lines:
        total += line.count("XMAS")
        total += line.count("SAMX")
    return total


def turn_grid(lines):
    ret = [""] * len(lines)
    for line in lines:
        i = 0
        for c in line:
            ret[i] += c
            i += 1
    return ret


def diagonal(lines):
    total = 0
    rows = len(lines)
    columns = len(lines[0])

    # Check for diagonals going down-right
    for y in range(rows - 3):  # Ensure room for downward diagonal
        for x in range(columns - 3):  # Ensure room for rightward diagonal
            diag = (
                lines[y][x]
                + lines[y + 1][x + 1]
                + lines[y + 2][x + 2]
                + lines[y + 3][x + 3]
            )
            if diag == "XMAS" or diag == "SAMX":
                total += 1

    # Check for diagonals going up-right
    for y in range(3, rows):  # Ensure room for upward diagonal
        for x in range(columns - 3):  # Ensure room for rightward diagonal
            diag = (
                lines[y][x]
                + lines[y - 1][x + 1]
                + lines[y - 2][x + 2]
                + lines[y - 3][x + 3]
            )
            if diag == "XMAS" or diag == "SAMX":
                total += 1

    return total


def x_mas(lines):
    total = 0
    rows = len(lines)
    columns = len(lines[0])

    y = 1
    while y < rows - 1:
        x = 1
        while x < columns - 1:
            if lines[y][x] != "A":
                x += 1
                continue
            a = lines[y - 1][x - 1] + "A" + lines[y + 1][x + 1]
            b = lines[y + 1][x - 1] + "A" + lines[y - 1][x + 1]
            if (a == "MAS" or a == "SAM") and (b == "MAS" or b == "SAM"):
                total += 1

            x += 1
        y += 1
    return total


print(f"Total horizontal: {horizontal(contents)}")
print(f"Total vertical: {horizontal(turn_grid(contents))}")
print(f"diagonal: {diagonal(contents)}")
print(
    f"total: {horizontal(contents) + horizontal(turn_grid(contents)) + diagonal(contents)}"
)

print(f"x-mas: {x_mas(contents)}")
# 1922 too high!
