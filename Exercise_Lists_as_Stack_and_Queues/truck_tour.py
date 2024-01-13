from collections import deque

total_petrol_stations = int(input())
pumps_info = deque([int(x) for x in input().split()] for x in range(total_petrol_stations))

fuel_in_tank = 0
start_index = 0

pumps_info_copy = pumps_info.copy()
while pumps_info_copy:
    fuel, distance = pumps_info_copy.popleft()
    fuel_in_tank += fuel
    if distance <= fuel_in_tank:
        fuel_in_tank -= distance
    else:
        start_index += 1
        fuel_in_tank = 0
        pumps_info.rotate(-1)
        pumps_info_copy = pumps_info.copy()   # if not copied, this also change the original list when line 11 pop!

print(start_index)





