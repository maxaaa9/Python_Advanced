row, col = [int(x) for x in input().split()]

matrix = [[r for r in input().split()] for r in range(row)]

identical_matrix = 0

for r in range(row - 1):
    for c in range(col - 1):
        current_el = matrix[r][c]
        right_el = matrix[r][c + 1]
        bottom_el = matrix[r + 1][c]
        bottom_right_el = matrix[r + 1][c + 1]
        identical_matrix += 1 if current_el == right_el == bottom_right_el == bottom_el else 0

print(identical_matrix)
