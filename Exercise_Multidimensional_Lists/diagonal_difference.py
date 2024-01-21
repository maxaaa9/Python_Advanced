matrix = [[int(x) for x in input().split()] for x in range(int(input()))]

primary_diagonal = [matrix[x][x] for x in range(len(matrix))]
secondary_diagonal = [matrix[x][len(matrix) - x - 1] for x in range(len(matrix))]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
