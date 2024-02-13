from collections import deque

armor = deque([int(x) for x in input().split(",")])
dmg = [int(x) for x in input().split(",")]
killed = 0

while armor and dmg:
    curr_armor = armor[0]
    curr_dmg = dmg[-1]

    if curr_dmg >= curr_armor:
        armor.popleft()
        dmg[-1] = curr_dmg - curr_armor
        killed += 1
        if dmg[-1] == 0:
            dmg.pop()
            continue

        elif len(dmg) > 1 and dmg[-1] > 0:
            dmg[-2] += dmg[-1]
            dmg.pop()

    else:
        armor[0] -= curr_dmg
        dmg.pop()
        armor.append(armor.popleft())

if not armor:
    print("All monsters have been killed!")
if not dmg:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed}")
