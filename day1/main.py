data = open("input.txt", "r").read()
numbers = [int(i) for i in data.split()]
left_numbers = []
right_numbers = []
i = 0

while i < len(numbers):
    if i % 2 == 0:
        left_numbers.append(numbers[i])
    else:
        right_numbers.append(numbers[i])
    i += 1


left_numbers.sort()
right_numbers.sort()
diff = sum([abs(l - r) for l, r in zip(left_numbers, right_numbers)])

print(f"Total difference: {diff}")


similarity = 0
for l in left_numbers:
    similarity += l * right_numbers.count(l)

print(f"The total similarity is {similarity}.")
