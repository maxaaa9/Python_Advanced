def even_odd_filter(**my_dictionary):
    if "odd" in my_dictionary.keys():
        my_dictionary["odd"] = [x for x in my_dictionary["odd"] if int(x) % 2 != 0]
    if "even" in my_dictionary.keys():
        my_dictionary["even"] = [x for x in my_dictionary["even"] if int(x) % 2 == 0]

    return dict(sorted(my_dictionary.items(), key=lambda x: -len(x[0])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
