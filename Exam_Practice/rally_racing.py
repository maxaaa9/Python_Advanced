movement = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}


size = int(input())
racing_number = input()
tunnels_coordinates = []
matrix = []

for row in range(size):
    matrix.append(input().split())
    if "T" in matrix[row]:
        tunnels_coordinates.append([row, matrix[row].index("T")])

car_position = [0, 0]
matrix[car_position[0]][car_position[1]] = "C"
total_km = 0

command = input()
while command != "End":

    go_to_row = car_position[0] + movement[command][0]
    go_to_col = car_position[1] + movement[command][1]

    matrix[car_position[0]][car_position[1]] = "."
    car_position = [go_to_row, go_to_col]
    if matrix[go_to_row][go_to_col] == "T":
        tunnels_coordinates.remove([go_to_row, go_to_col])
        matrix[car_position[0]][car_position[1]] = "."
        car_position = tunnels_coordinates[0]
        total_km += 30
    elif matrix[go_to_row][go_to_col] == "F":
        print(f"Racing car {racing_number} finished the stage!")
        matrix[car_position[0]][car_position[1]] = "C"
        total_km += 10
        break
    else:
        total_km += 10
    matrix[car_position[0]][car_position[1]] = "C"

    command = input()

else:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {total_km} km.")
[print(''.join(x)) for x in matrix]