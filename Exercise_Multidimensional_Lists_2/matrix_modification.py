row_col = int(input())

matrix = [[int(x) for x in input().split()] for x in range(row_col)]

command = input().split()

while command[0] != "END":

    operation, row, col, num = command[0], int(command[1]), int(command[2]), int(command[3])

    if 0 <= row < row_col and 0 <= col < row_col:
        if operation == "Add":
            matrix[row][col] += num
        elif operation == "Subtract":
            matrix[row][col] -= num

    else:
        print("Invalid coordinates")

    command = input().split()

[print(*rows) for rows in matrix]
