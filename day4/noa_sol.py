import re


def read_input(file_name):
    try:
        with open(file_name, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []


def count_horizontally(input_data):
    sum = 0
    for line in input_data:
        sum += line.count("XMAS")
        sum += line.count("SAMX")
    return sum


def rotate_matrix(grid):
    rows = len(grid)  # length of array of rows/how many rows there are
    cols = len(grid[0])  # length of each row
    rotated = []
    for col in range(cols - 1, -1, -1):  # voor elke collom
        new_row = ""
        for row in range(rows):
            new_row += grid[row][col]  # ga door de collom copy in een nieuw row
        rotated.append(new_row)  # zet nieuwe row bij resltaat

    return rotated


def count_diagonal_occurrences(grid):
    rows = len(grid)  # length of array of rows/how many rows there are
    cols = len(grid[0])  # length of each row
    count = 0
    word_len = len("xmas")  # xmas or samx(roept deze functie 2x aan)

    # Descending diagonal (top-left to bottom-right)
    for start_row in range(rows):  # Start at each row in the first column
        r, c = start_row, 0
        diagonal = ""
        while (
            r < rows and c < cols
        ):  # maakt string van diagonaal, doet <y=x(linksonder)
            diagonal += grid[r][c]
            r += 1
            c += 1
        count += diagonal.count("XMAS")  # Count occurrences of the word in the diagonal
        count += diagonal.count("SAMX")

    for start_col in range(1, cols):  # Start at each column in the first row
        r, c = 0, start_col
        diagonal = ""
        while r < rows and c < cols:  # doet >y=x(rechtsbovem)
            diagonal += grid[r][c]
            r += 1
            c += 1
        count += diagonal.count("XMAS")  # this doesnt work
        count += diagonal.count("SAMX")

    # Ascending diagonal (bottom-left to top-right)
    for start_row in range(
        rows
    ):  # Start at each row in the first column # start row doe je - maar begint op 0
        r, c = start_row, 0
        diagonal = ""
        while r >= 0 and c < cols:
            diagonal += grid[r][c]
            r -= 1  # was -=
            c += 1  # was +=
        count += diagonal.count("XMAS")
        count += diagonal.count("SAMX")

    for start_col in range(1, cols):  # Start at each column in the last row
        r, c = rows - 1, start_col
        diagonal = ""
        while r >= 0 and c < cols:
            diagonal += grid[r][c]
            r -= 1  # was -=
            c += 1  # was +=
        count += diagonal.count("XMAS")
        count += diagonal.count("SAMX")

    return count


if __name__ == "__main__":
    input_data = read_input("input.txt")

    found1 = count_horizontally(input_data)
    print("horizantally", found1)
    rotated = rotate_matrix(input_data)
    found2 = count_horizontally(rotated)
    print("vertically", found2)

    found3 = count_diagonal_occurrences(input_data)
    # found += count_diagonal_occurrences(input_data)
    print("diagnol", found3)
    #    print("input data = " + str(input_data))
