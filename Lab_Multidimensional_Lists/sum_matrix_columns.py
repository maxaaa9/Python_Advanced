row, col = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for x in range(row)]

for columns in range(col):
    column_sum = 0
    for rows in range(row):
        column_sum += matrix[rows][columns]
    print(column_sum)


