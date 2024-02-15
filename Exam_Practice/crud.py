directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

size = 6

matrix = [[x for x in input().split()] for x in range(size)]

my_position = [int(x) for x in input().strip("()").split(", ")]

commands = input().split(", ")
while commands[0] != "Stop":

    action, direction = commands[0], commands[1]

    go_to_row = my_position[0] + directions[direction][0]
    go_to_col = my_position[1] + directions[direction][1]

    if action == "Create":
        value = commands[2]
        if matrix[go_to_row][go_to_col] == ".":
            matrix[go_to_row][go_to_col] = f"{value}"

    elif action == "Update":
        value = commands[2]
        if matrix[go_to_row][go_to_col].isalnum():
            matrix[go_to_row][go_to_col] = f"{value}"

    elif action == "Delete":
        if matrix[go_to_row][go_to_col].isalnum():
            matrix[go_to_row][go_to_col] = "."

    elif action == "Read":
        if matrix[go_to_row][go_to_col].isalnum():
            print(matrix[go_to_row][go_to_col])

    my_position = [go_to_row, go_to_col]

    commands = input().split(", ")

[print(*row) for row in matrix]

