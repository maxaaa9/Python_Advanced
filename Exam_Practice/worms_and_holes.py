from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

fit = True
matches = 0
while worms and holes:
    worm = worms[-1]
    hole = holes[0]

    if worms[-1] <= 0:
        worms.pop()
        fit = False
        continue

    if worm == hole:
        worms.pop()
        holes.popleft()
        matches += 1

    else:
        worms[-1] -= 3
        holes.popleft()

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and fit:
    print("Every worm found a suitable hole!")

elif not worms and not fit:
    print("Worms left: none")

elif worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")
