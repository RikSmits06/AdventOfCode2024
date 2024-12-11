stones = open("input.txt", "r").read().split(" ")

tmp = {}
for stone in stones:
    if stone in tmp.keys():
        tmp[stone] += 1
    else:
        tmp[stone] = 1
stones = tmp


def blink(stones: dict):
    ret = {}
    for stone in stones.keys():
        if stone == "0":
            if "1" in ret.keys():
                ret["1"] += stones["0"]
            else:
                ret["1"] = stones["0"]
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            left = stone[:mid:]
            right = str(int(stone[mid::]))
            if left in ret.keys():
                ret[left] += stones[stone]
            else:
                ret[left] = stones[stone]
            if right in ret.keys():
                ret[right] += stones[stone]
            else:
                ret[right] = stones[stone]
        else:
            if str(int(stone) * 2024) in ret.keys():
                ret[str(int(stone) * 2024)] += stones[stone]
            else:
                ret[str(int(stone) * 2024)] = stones[stone]
    return ret


blinks = 75
while blinks > 0:
    stones = blink(stones)
    blinks -= 1

total = 0
for k in stones.keys():
    total += stones[k]
print(total)
