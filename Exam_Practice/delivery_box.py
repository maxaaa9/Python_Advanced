movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

rows, cols = [int(x) for x in input().split()]
starting_position = []

matrix = []
order = True
for row in range(rows):
    matrix.append(list(input()))
    if "B" in matrix[row]:
        starting_position = row, matrix[row].index("B")

current_position = starting_position
command = input()
while command:
    go_to_row = current_position[0] + movement[command][0]
    go_to_col = current_position[1] + movement[command][1]

    if not 0 <= go_to_row < rows or not 0 <= go_to_col < cols:
        print("The delivery is late. Order is canceled.")
        matrix[starting_position[0]][starting_position[1]] = " "
        break

    if matrix[go_to_row][go_to_col] == "*":
        command = input()
        continue

    if matrix[go_to_row][go_to_col] == "P":
        matrix[go_to_row][go_to_col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif matrix[go_to_row][go_to_col] == "-":
        matrix[go_to_row][go_to_col] = "."

    elif matrix[go_to_row][go_to_col] == "A":
        matrix[go_to_row][go_to_col] = "P"
        print("Pizza is delivered on time! Next order...")
        break

    current_position = go_to_row, go_to_col
    command = input()

[print(''.join(x)) for x in matrix]
