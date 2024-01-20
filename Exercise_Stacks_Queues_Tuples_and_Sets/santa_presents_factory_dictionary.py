from collections import deque

materials_for_toys = list(map(int, input().split()))
magic_level_deque = deque(map(int, input().split()))

required = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400,
}

crafted_toys = {}
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
    for toy in required:
        if required[toy] == product:
            if toy not in crafted_toys:
                crafted_toys[toy] = 0
            crafted_toys[toy] += 1
            is_equal = True
            break

    if product < 0:
        materials_for_toys.append(material + current_magic)

    elif not is_equal and product > 0:
        materials_for_toys.append(material + 15)

    if "Teddy bear" in crafted_toys.keys() and "Bicycle" in crafted_toys.keys():
        job_is_done = True
    if "Doll" in crafted_toys.keys() and "Wooden train" in crafted_toys.keys():
        job_is_done = True

if job_is_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_for_toys:
    print(f"Materials left: {', '.join(str(x) for x in materials_for_toys[::-1])}")

if magic_level_deque:
    print(f"Magic left: {', '.join(str(x) for x in magic_level_deque)}")

for toys, quantity in sorted(crafted_toys.items()):
    print(f"{toys}: {quantity}")