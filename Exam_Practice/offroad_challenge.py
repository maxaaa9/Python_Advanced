from collections import deque

initial_fuel = [int(x) for x in input().split()]    # stack
add_consumption = deque(int(x) for x in input().split())
needed_fuel = deque(int(x) for x in input().split())

reached_altitude = []
for run in range(1, len(initial_fuel) + 1):
    if initial_fuel and add_consumption and needed_fuel:
        total_consumption = initial_fuel[-1] - add_consumption[0]
        if total_consumption >= needed_fuel[0]:
            initial_fuel.pop()
            add_consumption.popleft()
            needed_fuel.popleft()
            reached_altitude.append(f"Altitude {run}")
            print(f"John has reached: Altitude {run}")

        elif total_consumption < needed_fuel[0]:
            print(f"John did not reach: Altitude {run}")
            break

if reached_altitude and needed_fuel:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(reached_altitude)}")

elif not reached_altitude:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")

elif not needed_fuel and reached_altitude:
    print("John has reached all the altitudes and managed to reach the top!")

