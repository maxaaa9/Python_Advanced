size = int(input())

positions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


money = 100
gambler_position = []
matrix = []

for g in range(size):
    matrix.append(list(input()))
    if "G" in matrix[g]:
        gambler_position = g, matrix[g].index("G")

command = input()

while command != "end":
    command_row, command_col = positions[command]

    go_to_row = gambler_position[0] + command_row
    go_to_col = gambler_position[1] + command_col

    if not 0 <= go_to_row < size and not 0 <= go_to_col < size:
        money = 0

    if matrix[go_to_row][go_to_col] == "W":
        money += 100

    elif matrix[go_to_row][go_to_col] == "P":
        money -= 200

    elif matrix[go_to_row][go_to_col] == "J":
        money += 100000
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {money}$")
        [print("".join(x)) for x in matrix]
        exit()

    if money <= 0:
        print("Game over! You lost everything!")
        exit()

    matrix[gambler_position[0]][gambler_position[1]] = "-"
    gambler_position = [go_to_row, go_to_col]
    matrix[gambler_position[0]][gambler_position[1]] = "G"

    command = input()

print(f"End of the game. Total amount: {money}$")
[print("".join(x)) for x in matrix]
