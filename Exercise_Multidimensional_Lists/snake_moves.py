from collections import deque

row, col = [int(x) for x in input().split()]

string = deque(input())

pop_list = string.copy()

for rows in range(row):
    while len(pop_list) < col:
        pop_list.extend(string)

    if rows % 2 == 0:
        print(*[pop_list.popleft() for x in range(col)], sep="")

    else:
        print(*[pop_list.popleft() for x in range(col)][::-1], sep="")


