matrix = [[int(x) for x in input().split(", ")] for x in range(int(input()))]

primary_diagonal = [matrix[x][x] for x in range(len(matrix))]
secondary_diagonal = [matrix[x][len(matrix) - x - 1] for x in range(len(matrix))]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")