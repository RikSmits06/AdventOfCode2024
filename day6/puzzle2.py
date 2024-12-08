class cell:
    visited = False
    obstacle = False
    visitCounter = 0

    def __init__(self, obstacle: bool):
        self.visited = False
        self.obstacle = obstacle

    def visit(self):
        self.visited = True
        self.visitCounter += 1

    def __str__(self):
        return "#" if self.obstacle else ("X" if self.visited else ".")

    def __repr__(self):
        return str(self)


total = 0

file_content = open("input.txt", "r").read()
map = [c for c in "".join(file_content.split("\n"))]

WIDTH = len(file_content.split("\n")[0])
HEIGHT = len(file_content.split("\n"))


def solve(map):
    cells: list[cell] = []
    pos = 0
    steps = 0
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
                cells[-1].visit()
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
        cells[y * WIDTH + x].visit()
        nextX = x + dx
        nextY = y + dy

        if steps > WIDTH * HEIGHT:
            return False

        if not inbound(nextX, nextY):
            return True

        nextCell = cells[nextY * WIDTH + nextX]

        if nextCell.obstacle:
            if dx == 0:
                dx, dy = -dy, dx
            else:
                dx, dy = dy, dx
            continue

        x = nextX
        y = nextY
    return True


i = 0
while i < len(map):
    new_map = map.copy()
    if new_map[i] != ".":
        i += 1
        continue

    new_map[i] = "#"
    solved = solve(new_map)
    if not solved:
        total += 1
    i += 1


print(total)
