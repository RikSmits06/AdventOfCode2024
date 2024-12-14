WIDTH = 101
MID_WIDTH = 50
HEIGHT = 103
MID_HEIGHT = 51


class Robot:
    x = None
    y = None
    dx = None
    dy = None

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self, s):
        self.x = (self.x + s * self.dx) % WIDTH
        self.y = (self.y + s * self.dy) % HEIGHT

    def quadrant(self):
        if self.x < MID_WIDTH:
            if self.y < MID_HEIGHT:
                return 1
            elif self.y > MID_HEIGHT:
                return 2
        elif self.x > MID_WIDTH:
            if self.y < MID_HEIGHT:
                return 3
            elif self.y > MID_HEIGHT:
                return 4
        return 0

    def __repr__(self):
        return f"p={self.x},{self.y} v={self.dx},{self.dy}"


contents = (
    open("input.txt", "r")
    .read()
    .replace("p=", " ")
    .replace(",", " ")
    .replace("v=", " ")
    .replace("\n", " ")
    .split(" ")
)
contents = [int(c) for c in contents if c != ""]
robots: list[Robot] = []


while len(contents) > 0:
    robots.append(
        Robot(contents.pop(0), contents.pop(0), contents.pop(0), contents.pop(0))
    )

quadrants = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}

for r in robots:
    r.move(100)
    quadrants[str(r.quadrant())] += 1
print(f"Total={quadrants["1"]*quadrants["2"]*quadrants["3"]*quadrants["4"]}")
