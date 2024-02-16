from collections import deque

caffeine = [int(x) for x in input().split(", ")]
energy_drink = deque([int(x) for x in input().split(", ")])
max_caffeine = 300
total_caffeine = 0

while caffeine and energy_drink:
    current_caffeine = caffeine[-1]
    current_energy_drink = energy_drink[0]
    multiply = current_caffeine * current_energy_drink

    if total_caffeine + multiply <= max_caffeine:
        caffeine.pop()
        energy_drink.popleft()
        total_caffeine += multiply

    else:
        caffeine.pop()
        energy_drink.append(energy_drink.popleft())
        total_caffeine -= 30
        if total_caffeine < 0:
            total_caffeine = 0

if energy_drink:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drink)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
