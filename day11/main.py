stones = [int(c) for c in open("input.txt", "r").read().split(" ")]


def blink(stones):
    result = []
    for stone in stones:
        if stone == 0:
            result.append(1)
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            firsthalf = int(str(stone)[:mid:])
            secondhalf = int(str(stone)[mid::])
            result.append(firsthalf)
            result.append(secondhalf)
        else:
            result.append(stone * 2024)
    return result


blinks = 25
while blinks > 0:
    print(blinks)
    stones = blink(stones)
    blinks -= 1

print(len(stones))
