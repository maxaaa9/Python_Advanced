def valid_position(c_row, c_col, size):
    return 0 <= c_row < size and 0 <= c_col < size


field_size = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

best_path = ""
final_path = {}
bunny_position = []
matrix = []

for row in range(field_size):
    matrix.append(input().split())
    if "B" in matrix[row]:
        bunny_position = [row, matrix[row].index("B")]

collected_eggs = float("-inf")

for direction, position in directions.items():
    row, col = [bunny_position[0] + position[0], bunny_position[1] + position[1]]

    current_eggs = 0
    path_coordinates = []

    while valid_position(row, col, field_size):
        if not matrix[row][col].isdigit():
            break

        current_eggs += int(matrix[row][col])
        path_coordinates.append([row, col])

        row += position[0]
        col += position[1]

    if current_eggs >= collected_eggs:
        collected_eggs = current_eggs
        final_path = path_coordinates
        best_path = direction

print(best_path)
[print(path) for path in final_path]
print(collected_eggs)
