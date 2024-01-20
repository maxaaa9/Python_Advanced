from collections import deque

materials_for_toys = list(map(int, input().split()))
magic_level_deque = deque(map(int, input().split()))

required = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

crafted_toys = []
job_is_done = False
while materials_for_toys and magic_level_deque:
    material = materials_for_toys.pop()
    current_magic = magic_level_deque.popleft()
    product = material * current_magic

    if current_magic == 0 and material == 0:
        continue

    elif current_magic == 0:
        materials_for_toys.append(material)
        continue

    elif material == 0:
        magic_level_deque.appendleft(current_magic)
        continue

    is_equal = False
    if product in required:
        crafted_toys.append(required[product])
        is_equal = True

    if product < 0:
        materials_for_toys.append(material + current_magic)

    elif not is_equal and product > 0:
        materials_for_toys.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted_toys) or {"Teddy bear", "Bicycle"}.issubset(crafted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_for_toys:
    print(f"Materials left: {', '.join(str(x) for x in materials_for_toys[::-1])}")

if magic_level_deque:
    print(f"Magic left: {', '.join(str(x) for x in magic_level_deque)}")

for item in sorted(set(crafted_toys)):
    print(f"{item}: {crafted_toys.count(item)}")
