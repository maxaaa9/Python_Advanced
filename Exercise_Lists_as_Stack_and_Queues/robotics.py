from collections import deque
from datetime import datetime, timedelta

robots = deque(input().split(";"))

robots_dict = {}

while robots:
    robot_info = robots.popleft()
    robot_name, time = robot_info.split("-")
    robots_dict[robot_name] = [int(time), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()
product = input()

while product != "End":
    products.append(product)
    product = input()

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()

    free_robots = []
    for robot, free_time in robots_dict.items():
        if free_time[1] > 0:
            robots_dict[robot][1] -= 1

        if free_time[1] == 0:
            free_robots.append([robot, free_time])

    if not free_robots:
        products.append(product)
        continue

    robot_name, info = free_robots[0]
    robots_dict[robot_name][1] = info[0]

    print(f"{robot_name} - {product} [{factory_time.strftime('%H:%M:%S')}]")
