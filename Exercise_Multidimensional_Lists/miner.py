size = int(input())

commands = input().split()

moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

total_coal = 0
collected_coal = 0
miner_pos = []
matrix = []

for rows in range(size):
    matrix.append(input().split())

    if "c" in matrix[rows]:
        total_coal += matrix[rows].count("c")

    if "s" in matrix[rows]:
        miner_pos = [rows, matrix[rows].index("s")]
        matrix[rows][miner_pos[1]] = "*"

for move in commands:
    r, c = miner_pos[0] + moves[move][0], miner_pos[1] + moves[move][1]

    if not (0 <= r < size and 0 <= c < size):
        continue

    miner_pos = [r, c]
    if matrix[r][c] == "c":
        collected_coal += 1
        if collected_coal == total_coal:
            print(f"You collected all coal! ({r}, {c})")
            break
    elif matrix[r][c] == "e":
        print(f"Game over! ({r}, {c})")
        break

    matrix[r][c] = "*"

else:
    print(f"{total_coal - collected_coal} pieces of coal left. {miner_pos[0], miner_pos[1]}")