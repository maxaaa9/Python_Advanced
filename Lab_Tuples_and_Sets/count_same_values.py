numbers = tuple([float(x) for x in input().split()])

unique_numbers = []
for unique in numbers:
    if unique not in unique_numbers:
        unique_numbers.append(unique)

for digit in unique_numbers:
    count = numbers.count(digit)
    print(f"{digit:.1f} - {count} times")
