garden = open("input.txt", "r").read().split("\n")
WIDTH = len(garden[0])
HEIGHT = len(garden)


def isValid(x, y):
    return x >= 0 and y >= 0 and x < WIDTH and y < HEIGHT


alreadyChecked = []


def getFenceArea(garden, x, y, checked=[], border=[]) -> int:
    global alreadyChecked
    checked.append((x, y))
    alreadyChecked.append((x, y))
    fences = 4
    crop = garden[y][x]
    if isValid(x, y - 1) and crop == garden[y - 1][x]:
        fences -= 1
        if not (x, y - 1) in checked:
            fences += getFenceArea(garden, x, y - 1, checked, border)[0]
    else:
        border.append((x, y, "up"))
    if isValid(x, y + 1) and crop == garden[y + 1][x]:
        fences -= 1
        if not (x, y + 1) in checked:
            fences += getFenceArea(garden, x, y + 1, checked, border)[0]
    else:
        border.append((x, y, "down"))
    if isValid(x - 1, y) and crop == garden[y][x - 1]:
        fences -= 1
        if not (x - 1, y) in checked:
            fences += getFenceArea(garden, x - 1, y, checked, border)[0]
    else:
        border.append((x, y, "left"))
    if isValid(x + 1, y) and crop == garden[y][x + 1]:
        fences -= 1
        if not (x + 1, y) in checked:
            fences += getFenceArea(garden, x + 1, y, checked, border)[0]
    else:
        border.append((x, y, "right"))
    return (fences, len(checked), border)


def printPrice():
    price = 0
    y = 0
    while y < HEIGHT:
        x = 0
        while x < WIDTH:
            if not (x, y) in alreadyChecked:
                fences, area, _ = getFenceArea(garden[::], x, y, checked=[], border=[])
                price += fences * area
            x += 1
        y += 1
    print(f"Normal price is: {price}")


def printPriceV2():
    price = 0
    y = 0
    while y < HEIGHT:
        x = 0
        while x < WIDTH:
            if not (x, y) in alreadyChecked:
                fences, area, borders = getFenceArea(
                    garden[::], x, y, checked=[], border=[]
                )
                price += totalSides(borders) * area
            x += 1
        y += 1
    print(f"Bulk price is: {price}")


def calcSidesDiff(group):
    if len(group) == 1:
        return 1
    sides = 0
    i = 0
    last = -10
    while i < len(group):
        if group[i] - last != 1:
            sides += 1
        last = group[i]
        i += 1
    return sides


def sidesLeft(borders):
    sides = 0
    sortedborders = [(c[0], c[1]) for c in borders if c[2] == "left"]
    groups = {}
    for b in sortedborders:
        if b[0] in groups.keys():
            groups[b[0]].append(b[1])
        else:
            groups[b[0]] = [b[1]]
    for group in groups.values():
        group.sort()
        sides += calcSidesDiff(group)
    return sides


def sidesRight(borders):
    sides = 0
    sortedborders = [(c[0], c[1]) for c in borders if c[2] == "right"]
    groups = {}
    for b in sortedborders:
        if b[0] in groups.keys():
            groups[b[0]].append(b[1])
        else:
            groups[b[0]] = [b[1]]
    for group in groups.values():
        group.sort()
        sides += calcSidesDiff(group)
    return sides


def sidesUp(borders):
    sides = 0
    sortedborders = [(c[0], c[1]) for c in borders if c[2] == "up"]
    groups = {}
    for b in sortedborders:
        if b[1] in groups.keys():
            groups[b[1]].append(b[0])
        else:
            groups[b[1]] = [b[0]]
    for group in groups.values():
        group.sort()
        sides += calcSidesDiff(group)
    return sides


def sidesDown(borders):
    sides = 0
    sortedborders = [(c[0], c[1]) for c in borders if c[2] == "down"]
    groups = {}
    for b in sortedborders:
        if b[1] in groups.keys():
            groups[b[1]].append(b[0])
        else:
            groups[b[1]] = [b[0]]
    for group in groups.values():
        group.sort()
        sides += calcSidesDiff(group)
    return sides


def totalSides(borders):
    return (
        sidesDown(borders) + sidesLeft(borders) + sidesRight(borders) + sidesUp(borders)
    )


printPriceV2()
