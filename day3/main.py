import re

contents = open("input.txt").read()
matches = re.findall("(mul\\(\\d+,\\d+\\))|(do\\(\\))|(don't\\(\\))", contents)

total = 0
blocked = False
for mul, do, dont in matches:
    if mul and not blocked:
        [left, right] = mul.split(",")
        right = int(right[0:-1:])
        left = int(left[4::])
        total += right * left
    if do:
        blocked = False
    if dont:
        blocked = True

print(total)
