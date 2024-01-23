row, col = [int(x) for x in input().split()]
start_symbol = ord('a')

for r in range(row):
    for c in range(col):
        print(f"{chr(start_symbol + r)}{chr(start_symbol + r + c)}{chr(start_symbol + r)}", end=" ")
    print()