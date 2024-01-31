def position_validator(pos_r, pos_c, size) -> bool:
    if 0 <= pos_c < size and 0 <= pos_r < size:
        return True
    return False


table_size = int(input())

matrix = [[x for x in list(input())] for _ in range(table_size)]

moves = ([-2, 1],   #top-right
         [-2, -1],   #top-left
         [-1, -2],  #left-top
         [1, -2],   #left-bot
         [2, -1],   #bot-left
         [2, 1],    #bot-right
         [1, 2],    #right-bot
         [-1, 2])   #right-top

removed_knights = 0

while True:
    total_attacks = 0
    most_powerful_knight = []

    for row in range(table_size):
        for col in range(table_size):
            if matrix[row][col] == "K":
                attacks = 0

                for r, c in moves:
                    current_row = row + r
                    current_col = col + c

                    if position_validator(current_row, current_col, table_size):
                        if matrix[current_row][current_col] == "K":
                            attacks += 1

                if attacks > total_attacks:
                    most_powerful_knight = [row, col]
                    total_attacks = attacks

    if most_powerful_knight:
        matrix[most_powerful_knight[0]][most_powerful_knight[1]] = "0"
        removed_knights += 1
    else:
        print(removed_knights)
        break
