matrix_rows = int(input())
even_matrix = []

for row in range(matrix_rows):
    even_matrix.append(list(int(x) for x in input().split(", ") if int(x) % 2 == 0))

print(even_matrix)