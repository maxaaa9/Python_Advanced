def map_validator(current_row, current_col, map_size):
    if not 0 <= current_row < map_size or not 0 <= current_col < map_size:
        return True
    return False


mapping = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

size = int(input())

matrix = []
burrows_coordinates = []
snake_pos = []
for row in range(size):
    matrix.append(list(input()))
    if "S" in matrix[row]:
        snake_pos = row, matrix[row].index("S")
    for b in matrix[row]:
        if b == "B":
            burrows_coordinates.append([row, matrix[row].index(b)])


collected_food = 0

while True:
    command = input()

    r = snake_pos[0] + mapping[command][0]
    c = snake_pos[1] + mapping[command][1]
    matrix[snake_pos[0]][snake_pos[1]] = "."
    snake_pos = [r, c]
    if map_validator(r, c, size):
        print("Game over!")
        break

    elif matrix[r][c] == "B":
        burrows_coordinates.remove([r, c])
        snake_pos = burrows_coordinates[0]

    elif matrix[r][c] == "*":
        collected_food += 1
        if collected_food == 10:
            matrix[snake_pos[0]][snake_pos[1]] = "S"
            break

    matrix[r][c] = "."


if collected_food == 10:
    print("You won! You fed the snake.")

print(f"Food eaten: {collected_food}")
[print(''.join(m)) for m in matrix]
