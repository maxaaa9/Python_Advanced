from collections import deque

quantity_of_water = int(input())

people = deque()
while True:
    people_for_water = input()
    if people_for_water == "Start":
        break
    people.append(people_for_water)

while True:
    command = input().split()
    if command[0].isdigit():
        quantity = int(command[0])
        if quantity <= quantity_of_water:
            quantity_of_water -= quantity
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")
    elif command[0] == "refill" and command[1].isdigit():
        quantity_of_water += int(command[1])

    elif command[0] == "End":
        print(f"{quantity_of_water} liters left")
        break

