def position_validator(idx_row, idx_col, matrix_size) -> bool:
    statement = True
    if idx_row < 0 or idx_row >= matrix_size:
        statement = False
    if idx_col < 0 or idx_col >= matrix_size:
        statement = False
    return statement


size = int(input())

direction = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix = []
alice_position = []
total_tea_bags = 0

for rows in range(size):
    matrix.append(input().split())
    if "A" in matrix[rows]:
        alice_position = rows, matrix[rows].index("A")
        matrix[alice_position[0]][alice_position[1]] = "*"

collection_successful = True
while total_tea_bags < 10:
    command = input()

    row, col = alice_position[0] + direction[command][0], alice_position[1] + direction[command][1]

    if not position_validator(row, col, size):
        collection_successful = False
        break

    alice_position = row, col

    if matrix[row][col].isdigit():
        total_tea_bags += int(matrix[row][col])

    if matrix[row][col] == "R":
        matrix[alice_position[0]][alice_position[1]] = "*"
        collection_successful = False
        break

    matrix[alice_position[0]][alice_position[1]] = "*"

if not collection_successful:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
[print(*row) for row in matrix]

