from collections import deque

clothes_deque = deque(int(x) for x in input().split())
rack_capacity = int(input())

rack_counter = 1
current_rack_capacity = rack_capacity
while clothes_deque:
    current_cloth_size = clothes_deque.popleft()
    if current_rack_capacity < current_cloth_size:
        current_rack_capacity = rack_capacity
        rack_counter += 1
    current_rack_capacity -= current_cloth_size

else:
    print(rack_counter)
