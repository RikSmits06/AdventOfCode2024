contents = open("input.txt", "r").read()
grid = contents.split("\n")
WIDTH = len(grid[0])
HEIGHT = len(grid)

tmp = []
for g in grid:
    tmp.append([int(c) if c != "." else -100 for c in g])
grid = tmp


def validIndex(x, y):
    return x >= 0 and y >= 0 and x < WIDTH and y < HEIGHT


def reachNine(pt, collect):
    x = pt[0]
    y = pt[1]
    if grid[y][x] == 9:
        a.append(pt)
    else:
        cur = grid[y][x]
        if validIndex(x, y - 1) and grid[y - 1][x] - cur == 1:
            reachNine((x, y - 1), collect)
        if validIndex(x - 1, y) and grid[y][x - 1] - cur == 1:
            reachNine((x - 1, y), collect)
        if validIndex(x + 1, y) and grid[y][x + 1] - cur == 1:
            reachNine((x + 1, y), collect)
        if validIndex(x, y + 1) and grid[y + 1][x] - cur == 1:
            reachNine((x, y + 1), collect)


total = 0
y = 0
while y < HEIGHT:
    x = 0
    while x < WIDTH:
        a = []
        if grid[y][x] == 0:
            reachNine((x, y), a)
            total += len(a)
        x += 1
    y += 1
print(total)
