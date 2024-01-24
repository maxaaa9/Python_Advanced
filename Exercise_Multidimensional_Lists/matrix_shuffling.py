def valid_moves(move_coordinate, rows, cols):
    return ({move_coordinate[0] and move_coordinate[2]}.issubset(rows) and
            {move_coordinate[1] and move_coordinate[3]}.issubset(cols))


def swap_coordinates(swap_matrix, moves, val_row, val_col):
    if valid_moves(moves, val_row, val_col):
        row1, col1, row2, col2 = moves
        swap_matrix[row1][col1], swap_matrix[row2][col2] = swap_matrix[row2][col2], swap_matrix[row1][col1]
        [print(*r) for r in swap_matrix]
    else:
        print("Invalid input!")
    return swap_matrix


row, col = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(row)]

while True:
    command, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]

    valid_rows = range(row)
    valid_cols = range(col)

    if command == "END":
        break

    elif command == "swap" and len(coordinates) == 4:
        matrix = swap_coordinates(matrix, coordinates, valid_rows, valid_cols)

    else:
        print("Invalid input!")
