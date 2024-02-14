def movement_validator(x, y, row, col) -> bool:
    if 0 <= row < x and 0 <= col < y:
        return True
    return False


r, c = (int(x) for x in input().split(","))

mapping = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix = []
mouse_position = []
total_cheese = 0
for line in range(r):
    matrix.append(list(input()))
    if "M" in matrix[line]:
        mouse_position = line, matrix[line].index("M")
    if "C" in matrix[line]:
        total_cheese += matrix[line].count("C")

command = input()
game_over = False
while command != "danger":

    go_to_row = mouse_position[0] + mapping[command][0]
    go_to_col = mouse_position[1] + mapping[command][1]

    if not movement_validator(r, c, go_to_row, go_to_col):
        print("No more cheese for tonight!")
        break

    if matrix[go_to_row][go_to_col] == "C":
        total_cheese -= 1
        if total_cheese == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            game_over = True

    elif matrix[go_to_row][go_to_col] == "@":
        command = input()
        continue

    elif matrix[go_to_row][go_to_col] == "T":
        print("Mouse is trapped!")
        game_over = True

    matrix[mouse_position[0]][mouse_position[1]] = "*"
    mouse_position = [go_to_row, go_to_col]
    matrix[mouse_position[0]][mouse_position[1]] = "M"

    if game_over:
        break

    command = input()

if total_cheese and command == "danger":
    print("Mouse will come back later!")

[print(''.join(x)) for x in matrix]

