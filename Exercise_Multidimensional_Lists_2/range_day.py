rows = 5
cols = 5

move_coordinates = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
}

my_position = []
matrix = []
total_targets = 0
targets_coordinate = []
target_hits = 0


for x in range(rows):
    matrix.append(input().split())
    if "A" in matrix[x]:
        my_position = x, matrix[x].index("A")
    if "x" in matrix[x]:
        total_targets += matrix[x].count("x")

for command in range(int(input())):
    action = input().split()

    if action[0] == "move":
        direction = move_coordinates[action[1]]
        steps = int(action[2])

        new_location = my_position[0] + direction[0] * steps, my_position[1] + direction[1] * steps
        if 0 <= new_location[0] < rows and 0 <= new_location[1] < cols:
            if not matrix[new_location[0]][new_location[1]] == "x":
                matrix[my_position[0]][my_position[1]] = "."
                my_position = new_location
                matrix[new_location[0]][new_location[1]] = "A"

    if action[0] == "shoot":
        direction = move_coordinates[action[1]]
        r = my_position[0] + direction[0]
        c = my_position[1] + direction[1]

        while 0 <= r < rows and 0 <= c < cols:
            if matrix[r][c] == "x":
                matrix[r][c] = "."
                target_hits += 1
                targets_coordinate.append([r, c])
                break

            r += direction[0]
            c += direction[1]

    if target_hits == total_targets:
        print(f"Training completed! All {total_targets} targets hit.")
        break

if total_targets != target_hits:
    print(f"Training not completed! {total_targets - target_hits} targets left.")

[print(hit) for hit in targets_coordinate]


