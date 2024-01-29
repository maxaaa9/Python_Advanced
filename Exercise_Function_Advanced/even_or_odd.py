def even_odd(*args):
    if args[-1] == "even":
        my_list = [x for x in args[:-1] if int(x) % 2 == 0]
    else:
        my_list = [x for x in args[:-1] if int(x) % 2 != 0]

    return my_list


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
