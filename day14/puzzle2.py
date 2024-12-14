WIDTH = 101
MID_WIDTH = 50
HEIGHT = 103
MID_HEIGHT = 51

import PIL
import PIL.Image


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

im = PIL.Image.new("RGB", (WIDTH, HEIGHT))
t = 0
for _ in range(10000):
    posList = []
    for r in robots:
        r.move(1)
        posList.append((r.x, r.y))
    y = 0
    while y < HEIGHT:
        x = 0
        while x < WIDTH:
            c = (0, 255, 0) if (x, y) in posList else (0, 0, 0)
            im.putpixel((x, y), c)
            x += 1
        y += 1
    t += 1
    im.save(f".\images\img_{t}.png")
