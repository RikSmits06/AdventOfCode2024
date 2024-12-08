reports = open("input.txt").read().split("\n")
reports.pop()


def isSafe(levels, increasing=None, skipped=False):
    if len(levels) <= 1:
        return True
    diff = levels[1] - levels[0]
    if increasing == None:
        return True and isSafe(levels, increasing=(abs(diff) == diff), skipped=skipped)
    elif diff > 0 and diff <= 3 and increasing:
        return True and isSafe(levels[1::], increasing=True, skipped=skipped)
    elif diff < 0 and diff >= -3 and not increasing:
        return True and isSafe(levels[1::], increasing=False, skipped=skipped)
    return False


i = 0
for report in reports:
    levels = [int(i) for i in report.split()]
    if isSafe(levels):
        i += 1
    else:
        j = 0
        while j < len(levels):
            tmp = levels.copy()
            del tmp[j]
            j += 1
            if isSafe(tmp):
                i += 1
                break


print(i)
