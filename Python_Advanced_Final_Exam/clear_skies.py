directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

size = int(input())

matrix = []
jet_position = []

total_enemy = 0
for row in range(size):
    matrix.append(list(input()))
    if "J" in matrix[row]:
        jet_position = [row, matrix[row].index("J")]
    if "E" in matrix[row]:
        total_enemy += matrix[row].count("E")

jet_armor = 300

while jet_armor != 0 and total_enemy != 0:
    command = input()

    r = jet_position[0] + directions[command][0]
    c = jet_position[1] + directions[command][1]

    if matrix[r][c] == "E":
        total_enemy -= 1
        if total_enemy == 0:
            print("Mission accomplished, you neutralized the aerial threat!")

        else:
            jet_armor -= 100
            if jet_armor == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{r}, {c}]!")

    elif matrix[r][c] == "R":
        jet_armor = 300

    matrix[r][c] = "-"
    matrix[jet_position[0]][jet_position[1]] = "-"
    jet_position = [r, c]
    matrix[r][c] = "J"

[print(''.join(x)) for x in matrix]
