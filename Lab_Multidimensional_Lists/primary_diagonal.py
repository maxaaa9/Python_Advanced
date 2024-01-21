matrix_size = int(input())

matrix = [[int(x) for x in input().split()] for x in range(matrix_size)]

diagonal_sum = 0
for diagonal in range(matrix_size):
    row_index = diagonal
    column_index = diagonal
    diagonal_sum += matrix[row_index][column_index]

print(diagonal_sum)
