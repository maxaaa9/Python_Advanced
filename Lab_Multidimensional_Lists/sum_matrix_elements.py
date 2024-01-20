row, col = [int(x) for x in input().split(", ")]

total_sum = 0

matrix = []

for i in range(row):
    rows = [int(x) for x in input().split(", ")]
    matrix.append(rows)
    total_sum += sum(rows)


print(total_sum)
print(matrix)