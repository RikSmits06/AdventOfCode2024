contents = open("input.txt", "r").read()


class space:
    empty: bool = None
    size: int = None
    number = 0

    def __init__(self, size, empty, number=0):
        self.empty = empty
        self.size = size
        self.number = str(number)


file_system: list[space] = []


count = 0
isEmpty = False
for c in contents:
    if not isEmpty:
        file_system.append(space(int(c), isEmpty, number=count))
        count += 1
    else:
        file_system.append(space(int(c), isEmpty))
    isEmpty = not isEmpty

i = len(file_system) - 1
while i >= 0:
    if file_system[i].empty:
        i -= 1
        continue
    j = 0
    while j < i:
        if file_system[j].empty and file_system[j].size >= file_system[i].size:
            tmp = file_system.pop(i)
            file_system.insert(i, space(tmp.size, empty=True))
            file_system[j].size -= file_system[i].size
            if file_system[j].size == 0:
                file_system.pop(j)
            file_system.insert(j, tmp)
            break
        j += 1
    i -= 1

numberList = []
for s in file_system:
    if not s.empty:
        numberList.extend([s.number] * s.size)
    else:
        numberList.extend([0] * s.size)

total = 0

for i, s in enumerate(numberList):
    total += i * int(s)

print(total)

# 69243662030 is too low.
# 87987830041 is too low.
