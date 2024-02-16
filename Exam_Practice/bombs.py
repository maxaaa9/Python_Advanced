from collections import deque

bomb_effect = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

bombs = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120,
}

crafted_bombs = {
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0,
}

bombs_pouch = False
while bomb_effect and bomb_casings:
    current_effect = bomb_effect[0]
    current_casings = bomb_casings[-1]
    current_sum = current_casings + current_effect

    if current_sum in bombs.values():
        for bomb in bombs:
            if current_sum == bombs[bomb]:
                crafted_bombs[bomb] += 1
                break
        bomb_effect.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

    if all(x >= 3 for x in crafted_bombs.values()):
        bombs_pouch = True
        break


if bombs_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effect:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effect)}")

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")

for bomb, quantity in crafted_bombs.items():
    print(f"{bomb}: {quantity}")
