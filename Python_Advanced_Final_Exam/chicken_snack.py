from collections import deque

money = [int(x) for x in input().split()]
price_for_food = deque(int(x) for x in input().split())

food_target_count = 4
food_counter = 0

while money and price_for_food:
    current_money = money[-1]
    current_price = price_for_food[0]

    if current_money == current_price:
        food_counter += 1

    elif current_money > current_price:
        food_counter += 1
        difference = current_money - current_price
        money.pop()
        price_for_food.popleft()
        if money:
            money[-1] += difference

        continue

    money.pop()
    price_for_food.popleft()

if food_counter >= food_target_count:
    print(f"Gluttony of the day! Henry ate {food_counter} foods.")

elif food_counter == 1:
    print("Henry ate: 1 food.")

elif food_counter:
    print(f"Henry ate: {food_counter} foods.")

else:
    print("Henry remained hungry. He will try next weekend again.")