from collections import deque
names = deque(input().split())
number = int(input())

counter = 1
while len(names) != 1:
    if counter == number:
        print(f"Removed {names.popleft()}")
        counter = 1
    else:
        names.append(names.popleft())
        counter += 1

print(f"Last is {''.join(names)}")
