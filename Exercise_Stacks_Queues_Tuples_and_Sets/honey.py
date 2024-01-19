from collections import deque

working_bees = deque(map(int, input().split()))
nectars = list(map(int, input().split()))
symbols = deque(input().split())

functions = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "/": lambda a, b: a / b if b != 0 else 0,
    "*": lambda a, b: a * b,
}

total_honey = 0

while working_bees and nectars:
    bee = working_bees.popleft()
    nectar = nectars.pop()
    if nectar >= bee:
        symbol = symbols.popleft()
        total_honey += abs(functions[symbol](bee, nectar))
    elif nectar < bee:
        working_bees.appendleft(bee)

print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")

if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")
