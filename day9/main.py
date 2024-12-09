contents = open("input.txt", "r").read()

# Prepping input.
empty = False

fileSystem = []
count = 0

for c in contents:
    for _ in range(int(c)):
        if empty:
            fileSystem.append(".")
        else:
            fileSystem.append(str(count))

    if not empty:
        count += 1
    empty = not empty


# Compressing
def removeTrailing(inp: list[str]):
    while inp[-1] == ".":
        inp.pop()


i = 0
removeTrailing(fileSystem)
while i < len(fileSystem):
    if fileSystem[i] == ".":
        fileSystem[i], fileSystem[-1] = fileSystem[-1], fileSystem[i]
    i += 1
    removeTrailing(fileSystem)

# Calculating sum.
total = 0

for i, num in enumerate(fileSystem):
    total += i * int(num)

print(total)
