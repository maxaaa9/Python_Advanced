from collections import deque

egg_size = deque([int(x) for x in input().split(", ")])
paper_size = deque([int(x) for x in input().split(", ")])

box_size = 50
total_boxes = 0

while egg_size and paper_size:
    current_egg = egg_size[0]
    current_paper = paper_size[-1]

    if current_egg <= 0:
        egg_size.popleft()
        continue

    elif current_egg == 13:
        egg_size.popleft()
        first_paper = paper_size.popleft()
        last_paper = paper_size.pop()
        paper_size.append(first_paper)
        paper_size.appendleft(last_paper)
        continue

    elif current_egg + current_paper <= box_size:
        total_boxes += 1

    egg_size.popleft()
    paper_size.pop()

if total_boxes:
    print(f"Great! You filled {total_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_size:
    print(f"Eggs left: {', '.join(str(x) for x in egg_size)}")
if paper_size:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_size)}")