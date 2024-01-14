parking_data = set()

for car in range(int(input())):
    direction, number = input().split(", ")
    if direction == "IN" and number not in parking_data:
        parking_data.add(number)
    elif direction == "OUT" and number in parking_data:
        parking_data.remove(number)

if parking_data:
    for car in parking_data:
        print(car)
else:
    print("Parking Lot is Empty")

