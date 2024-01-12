my_stack = []

for _ in range(int(input())):
    data = input().split()
    if len(data) > 1 and data[0] == "1":
        integer = data[1]
        my_stack.append(integer)
    elif my_stack:
        command = data[0]
        if command == "2":
            my_stack.pop()
        elif command == "3":
            print(max(my_stack))
        elif command == "4":
            print(min(my_stack))

else:
    print(*my_stack[::-1], sep=", ")



