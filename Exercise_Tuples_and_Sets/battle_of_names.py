odd_set = set()
even_set = set()

for counter in range(1, int(input()) + 1):
    name = input()
    ascii_sum = 0
    for i in name:
        ascii_sum += ord(i)
    ascii_sum //= counter
    if ascii_sum % 2 != 0:
        odd_set.add(ascii_sum)
    else:
        even_set.add(ascii_sum)

if sum(odd_set) == sum(even_set):
    print(", ".join([str(x) for x in odd_set.union(even_set)]))

elif sum(odd_set) > sum(even_set):
    print(", ".join([str(x) for x in odd_set.difference(even_set)]))

else:
    print(", ".join([str(x) for x in odd_set.symmetric_difference(even_set)]))