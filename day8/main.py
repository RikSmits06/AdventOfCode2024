contents = open("input.txt", "r").read()

map: list[str] = contents.split("\n")
WIDTH = len(map[0])
HEIGHT = len(map)

all_unique_chars = []
for c in contents:
    if c == "." or c == "\n" or c in all_unique_chars:
        continue
    all_unique_chars.append(c)


def allPositions(map, char):
    ret = []
    y = 0
    while y < HEIGHT:
        x = 0
        while x < WIDTH:
            if map[y][x] == char:
                ret.append((x, y))
            x += 1
        y += 1
    return ret


antennaPositions = []


def addAntennaPosition(pos):
    if pos[0] < 0 or pos[0] >= WIDTH or pos[1] < 0 or pos[1] >= HEIGHT:
        return
    if pos in antennaPositions:
        return
    antennaPositions.append(pos)


for uchar in all_unique_chars:
    positions = allPositions(map, uchar)
    i = 0
    while i < len(positions):
        j = len(positions) - 1
        while j > i:
            p1 = positions[i]
            p2 = positions[j]

            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]

            for t in range(WIDTH):
                addAntennaPosition((p1[0] + dx * t, p1[1] + dy * t))
                addAntennaPosition((p2[0] - dx * t, p2[1] - dy * t))

            j -= 1
        i += 1

print(len(antennaPositions))
