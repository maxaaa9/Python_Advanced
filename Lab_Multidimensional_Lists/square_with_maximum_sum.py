rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(", ")] for x in range(rows)]

max_matrix = []
sum_of_matrix = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        current_digit = matrix[row][col]
        right_digit = matrix[row][col + 1]
        bottom_digit = matrix[row + 1][col]
        bottom_right_digit = matrix[row + 1][col + 1]

        current_sum = current_digit + right_digit + bottom_digit + bottom_right_digit
        if current_sum > sum_of_matrix:
            sum_of_matrix = current_sum
            max_matrix = [[current_digit, right_digit], [bottom_digit, bottom_right_digit]]

[print(*row) for row in max_matrix]
print(sum_of_matrix)