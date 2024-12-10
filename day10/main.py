contents = open("input.txt", "r").read()
grid = contents.split("\n")
WIDTH = len(grid[0])
HEIGHT = len(grid)

tmp = []
for g in grid:
    tmp.append([int(c) if c != "." else -1 for c in g])
grid = tmp


def getTrailheads(map: list[list[int]], startx: int, starty: int) -> int:
    toCheck = [(startx, starty)]
    total = 0

    i = 0
    while i < WIDTH * HEIGHT * 10:
        current_pos = toCheck[0]
        current_x = current_pos[0]
        current_y = current_pos[1]
        current_value = map[current_y][current_x]

        if current_y > 0 and current_value + 1 == map[current_y - 1][current_x]:
            a = (current_x, current_y - 1)
            if a not in toCheck:
                toCheck.append(a)
        if current_y + 1 < WIDTH and current_value + 1 == map[current_y + 1][current_x]:
            a = (current_x, current_y + 1)
            if a not in toCheck:
                toCheck.append(a)
        if current_x > 0 and current_value + 1 == map[current_y][current_x - 1]:
            a = (current_x - 1, current_y)
            if a not in toCheck:
                toCheck.append(a)
        if current_x + 1 < WIDTH and current_value + 1 == map[current_y][current_x + 1]:
            a = (current_x + 1, current_y)
            if a not in toCheck:
                toCheck.append(a)

        i += 1
        toCheck.append(toCheck.pop(0))
    for x, y in toCheck:
        value = map[y][x]
        if value == 9:
            total += 1
    return total


# print(getTrailheads(grid, 5, 6))
total = 0

y = 0
while y < HEIGHT:
    x = 0
    while x < WIDTH:
        if grid[y][x] == 0:
            total += getTrailheads(grid, x, y)
        x += 1
    y += 1
print(total)
