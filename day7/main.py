equations = open("input.txt", "r").read().split("\n")


class Infix:
    def __init__(self, function):
        self.function = function

    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))

    def __or__(self, other):
        return self.function(other)

    def __rlshift__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))

    def __rshift__(self, other):
        return self.function(other)

    def __call__(self, value1, value2):
        return self.function(value1, value2)


def increase(operators):
    i = 0
    while i < len(operators):
        if operators[i] == 2:
            operators[i] = 0
            i += 1
        else:
            operators[i] += 1
            break


def getOpp(num):
    if num == 0:
        return "+"
    elif num == 1:
        return "*"
    return "|x|"


x = Infix(lambda x, y: int(str(x) + str(y)))


def isSolvable(eqTotal, eqNumbers):
    operatorsRequired = len(eqNumbers) - 1
    # false = "+", true = "*"
    operators = [0] * operatorsRequired
    for _ in range(3**operatorsRequired):
        tmpOpp = operators.copy() + [None]
        evalString = ""
        j = operatorsRequired
        for opp, num in zip(tmpOpp, eqNumbers):
            if opp == None:
                evalString += f"{num})"
                continue
            if j != 0:
                evalString += f"{''.join(['('] * j)}{num}{getOpp(opp)}"
                j = 0
                continue
            evalString += f"{num}){getOpp(opp)}"
        if eval(evalString) == eqTotal:
            return True
        increase(operators)
    return False


total = 0
for equation in equations:
    splitted = equation.split(":")
    eqTotal = int(splitted[0])
    eqNumbers = [int(c) for c in splitted[1].split()]
    if isSolvable(eqTotal, eqNumbers):
        total += eqTotal

print(total)
# 113978869623 - answer is too low.
