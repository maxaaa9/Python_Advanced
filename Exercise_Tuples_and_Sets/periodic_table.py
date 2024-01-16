elements_set = set()

for el_row in range(int(input())):
    elements = input().split()
    for element in elements:
        elements_set.add(element)

else:
    print(*(elements_set), sep='\n')
