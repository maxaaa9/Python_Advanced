def list_manipulator(digit_list, command, action, *args):
    if command == "add" and action == "beginning":
        digit_list = list(args) + digit_list

    elif command == "add" and action == "end":
        digit_list = digit_list + list(args)

    elif command == "remove" and action == "beginning":
        if args:
            digit = int(*args)
            digit_list = digit_list[digit:]
        else:
            del digit_list[0]

    elif command == "remove" and action == "end":
        if args:
            for delete in range(*args):
                digit_list.pop()
        else:
            digit_list.pop()

    return digit_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

