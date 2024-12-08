class cell:
    visited = False
    obstacle = False

    def __init__(self, obstacle: bool):
        self.visited = False
        self.obstacle = obstacle

    def __str__(self):
        return "#" if self.obstacle else ("X" if self.visited else ".")

    def __repr__(self):
        return str(self)


file_content = open("input.txt", "r").read()
map = [c for c in "".join(file_content.split("\n"))]

WIDTH = len(file_content.split("\n")[0])
HEIGHT = len(file_content.split("\n"))

cells: list[cell] = []
pos = 0

dx = 0
dy = 0

for m in map:
    match m:
        case ".":
            cells.append(cell(False))
        case "#":
            cells.append(cell(True))
        case "<" | ">" | "^" | "v":
            pos = map.index(m)
            cells.append(cell(False))
            cells[-1].visited = True
            match m:
                case "^":
                    dx = 0
                    dy = -1
                case ">":
                    dx = 1
                    dy = 0
                case "v":
                    dx = 0
                    dy = 1
                case "<":
                    dx = -1
                    dy = 0

x = pos % WIDTH
y = int((pos - x) / WIDTH)


def inbound(x, y):
    return x >= 0 and x < WIDTH and y >= 0 and y < HEIGHT


while inbound(x, y):
    cells[y * WIDTH + x].visited = True
    nextX = x + dx
    nextY = y + dy

    if not inbound(nextX, nextY):
        break

    nextCell = cells[nextY * WIDTH + nextX]

    if nextCell.obstacle:
        if dx == 0:
            dx, dy = -dy, dx
        else:
            dx, dy = dy, dx
        continue

    x = nextX
    y = nextY

total = 0

for c in cells:
    if c.visited:
        total += 1

print(total)
