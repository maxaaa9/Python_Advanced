from collections import deque

player = deque(input().split(", "))

matrix_size = 6

matrix = [[x for x in input().split()] for _ in range(matrix_size)]

stunned_players = []

while True:
    current_player = player[0]
    player_location = [int(x) for x in input().strip("()").split(", ")]
    player.rotate(1)

    if current_player in stunned_players:
        stunned_players.remove(current_player)
        continue

    if matrix[player_location[0]][player_location[1]] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        exit()

    elif matrix[player_location[0]][player_location[1]] == "T":
        print(f"{current_player} is out of the game! The winner is {player.popleft()}.")
        exit()

    elif matrix[player_location[0]][player_location[1]] == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        stunned_players.append(current_player)

