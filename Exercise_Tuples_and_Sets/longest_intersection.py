intersection_data = set()

for _ in range(int(input())):
    first_set_range, second_set_range = [el.split(",") for el in input().split("-")]

    first_set = set(int(x) for x in range(int(first_set_range[0]), int(first_set_range[1]) + 1))
    second_set = set(int(x) for x in range(int(second_set_range[0]), int(second_set_range[1]) + 1))
    set_intersection = first_set.intersection(second_set)
    if len(set_intersection) > len(intersection_data):
        intersection_data = set_intersection

print(f"Longest intersection is"
      f" [{', '.join(str(x) for x in intersection_data)}]"
      f" with length {len(intersection_data)}")