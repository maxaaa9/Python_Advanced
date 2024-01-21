matrix_size = int(input())

matrix = [[x for x in input()] for x in range(matrix_size)]

symbol = input()
result = tuple()

for row in range(matrix_size):
    for col in range(matrix_size):
        if symbol in matrix[row][col]:
            result = (row, col)
    if result:
        print(result)
        exit()

print(f"{symbol} does not occur in the matrix")


