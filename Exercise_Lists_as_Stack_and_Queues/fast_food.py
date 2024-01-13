from collections import deque

food_quantity = int(input())
food_orders = deque(int(x) for x in input().split())

print(max(food_orders))

for digit in food_orders.copy():
    if digit <= food_quantity:
        food_quantity -= food_orders.popleft()

    else:
        print(f"Orders left: {' '.join(str(x) for x in food_orders)}")
        break
else:
    print("Orders complete")
