flatten_matrix = []

for _ in range(int(input())):
    flatten_matrix.extend(int(x) for x in input().split(", "))

print(flatten_matrix)