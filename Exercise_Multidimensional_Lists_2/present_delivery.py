def cookie_time(curr_row, curr_col, map_matrix, presents, directions, visit):
    for path, value in directions.items():
        r = curr_row + value[0]
        c = curr_col + value[1]
        if map_matrix[r][c].isalpha() and map_matrix[r][c] != "S":
            if map_matrix[r][c] == "V":
                visit += 1

            presents -= 1
            map_matrix[r][c] = "-"

        if presents <= 0:
            break

    return map_matrix, presents, visit


presents_number = int(input())

neighborhood = int(input())

move_coordinates = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
}

total_nice_kids = 0

santa_location = []
matrix = []

for rows in range(neighborhood):
    matrix.append(input().split())
    if "S" in matrix[rows]:
        santa_location = rows, matrix[rows].index("S")
    if "V" in matrix[rows]:
        total_nice_kids += matrix[rows].count("V")

visited_nice_kids = 0
commands = input()
while commands != "Christmas morning":

    move_row = santa_location[0] + move_coordinates[commands][0]
    move_col = santa_location[1] + move_coordinates[commands][1]

    if not 0 <= move_row < neighborhood and 0 <= move_col < neighborhood:
        continue

    if matrix[move_row][move_col] == "V":
        presents_number -= 1
        visited_nice_kids += 1
    elif matrix[move_row][move_col] == "C":
        matrix, presents_number, visited_nice_kids = \
            cookie_time(move_row, move_col, matrix, presents_number, move_coordinates, visited_nice_kids)

    matrix[santa_location[0]][santa_location[1]] = "-"
    santa_location = [move_row, move_col]

    if presents_number <= 0:
        break

    commands = input()

matrix[santa_location[0]][santa_location[1]] = "S"

if presents_number == 0 and total_nice_kids > visited_nice_kids:
    print("Santa ran out of presents!")

[print(*row) for row in matrix]
if total_nice_kids == visited_nice_kids:
    print(f"Good job, Santa! {visited_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - visited_nice_kids} nice kid/s.")


# HARD WAY!
def cookie_time(curr_row, curr_col, map_matrix, presents, directions, visit):
    for path, value in directions.items():
        r = curr_row + value[0]
        c = curr_col + value[1]
        if map_matrix[r][c].isalpha() and map_matrix[r][c] != "S":
            if map_matrix[r][c] == "V":
                visit += 1

            presents -= 1
            map_matrix[r][c] = "-"

        if presents <= 0:
            break

    return map_matrix, presents, visit


presents_number = int(input())

neighborhood = int(input())

move_coordinates = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
}

total_nice_kids = 0

santa_location = []
matrix = []

for rows in range(neighborhood):
    matrix.append(input().split())
    if "S" in matrix[rows]:
        santa_location = rows, matrix[rows].index("S")
    if "V" in matrix[rows]:
        total_nice_kids += matrix[rows].count("V")

visited_nice_kids = 0
commands = input()
while commands != "Christmas morning":

    move_row = santa_location[0] + move_coordinates[commands][0]
    move_col = santa_location[1] + move_coordinates[commands][1]

    if not 0 <= move_row < neighborhood and 0 <= move_col < neighborhood:
        continue

    if matrix[move_row][move_col] == "V":
        presents_number -= 1
        visited_nice_kids += 1
    elif matrix[move_row][move_col] == "C":
        matrix, presents_number, visited_nice_kids = \
            cookie_time(move_row, move_col, matrix, presents_number, move_coordinates, visited_nice_kids)

    matrix[santa_location[0]][santa_location[1]] = "-"
    santa_location = [move_row, move_col]
    matrix[santa_location[0]][santa_location[1]] = "S"

    if presents_number <= 0:
        break

    commands = input()

if presents_number == 0 and total_nice_kids > visited_nice_kids:
    print("Santa ran out of presents!")

[print(*row) for row in matrix]
if total_nice_kids == visited_nice_kids:
    print(f"Good job, Santa! {visited_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - visited_nice_kids} nice kid/s.")
