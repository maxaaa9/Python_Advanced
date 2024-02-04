def out_of_area(r, c, area):
    if r >= size:
        r = 0
    elif r < 0:
        r = area - 1

    if c >= size:
        c = 0
    elif c < 0:
        c = area - 1

    return r, c


size = int(input())

collected_fish_target = 20
move_commands = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
}

my_position = []
matrix = []


for row in range(size):
    matrix.append([x for x in input()])
    if "S" in matrix[row]:
        my_position = row, matrix[row].index("S")

collected_fish = 0
while True:
    command = input()

    if command == "collect the nets":
        break

    move_to_row = my_position[0] + move_commands[command][0]
    move_to_col = my_position[1] + move_commands[command][1]

    if not 0 <= move_to_row < size or not 0 <= move_to_col < size:
        move_to_row, move_to_col = out_of_area(move_to_row, move_to_col, size)

    if matrix[move_to_row][move_to_col].isdigit():
        collected_fish += int(matrix[move_to_row][move_to_col])

    elif matrix[move_to_row][move_to_col] == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
              f" Last coordinates of the ship: [{move_to_row},{move_to_col}]")
        exit()

    matrix[my_position[0]][my_position[1]] = "-"
    my_position = move_to_row, move_to_col
    matrix[my_position[0]][my_position[1]] = "S"

if collected_fish >= collected_fish_target:
    print("Success! You managed to reach the quota!")
else:
    difference = collected_fish_target - collected_fish
    print(f"You didn't catch enough fish and didn't reach the quota! You need {difference} tons of fish more.")

if collected_fish:
    print(f"Amount of fish caught: {collected_fish} tons.")
[print("".join(row)) for row in matrix]