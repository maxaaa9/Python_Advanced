row, col = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for x in range(row)]

matrix_sum = float("-inf")
biggest_matrix = []

for r in range(0, row - 2):
    for c in range(0, col - 2):
        row_one = matrix[r][c:c + 3]
        row_two = matrix[r + 1][c:c + 3]
        row_three = matrix[r + 2][c:c + 3]

        current_sum = sum(row_one) + sum(row_two) + sum(row_three)
        if current_sum > matrix_sum:
            matrix_sum = current_sum
            biggest_matrix = [row_one, row_two, row_three]

print(f"Sum = {matrix_sum}")
[print(*row) for row in biggest_matrix]

