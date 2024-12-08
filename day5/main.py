import re

contents = open("input.txt", "r").read()

rules = re.findall("\\d+\\|\\d+", contents)
rules = [rule.split("|") for rule in rules]

tmp = []
for rule in rules:
    tmp.append([int(rule[0]), int(rule[1])])
rules = tmp

b = False
pages = []
for line in contents.split("\n"):
    if line == "":
        b = True
        continue
    elif b:
        pages.append(line)
del b

tmp2 = []
for page in pages:
    tmp = []
    for n in page.split(","):
        tmp.append(int(n))
    tmp2.append(tmp)

pages = tmp2


def isCorrect(pages, rules):
    i = 0
    while i < len(pages):
        j = len(pages) - 1
        while j > i:
            if [pages[j], pages[i]] in rules:
                return False
            j -= 1
        i += 1
    return True


def orderCorrectly(pages, rules):
    while not isCorrect(pages, rules):
        i = 0
        while i < len(pages):
            j = len(pages) - 1
            while j > i:
                if [pages[j], pages[i]] in rules:
                    pages[j], pages[i] = pages[i], pages[j]
                j -= 1
            i += 1
    return pages


incorrectPages = []
totalCorrectly = 0
for page in pages:
    if isCorrect(page, rules):
        mid = int(len(page) / 2)
        totalCorrectly += page[mid]
    else:
        incorrectPages.append(page)
print(f"Total correctly ordered: {totalCorrectly}.")

totalNew = 0
for incPage in incorrectPages:
    correctOrder = orderCorrectly(incPage, rules)
    totalNew += correctOrder[int(len(incPage) / 2)]
print(f"Total incorrectly ordered now ordered: {totalNew}.")
