def concatenate(*args, **kwargs):
    new_string = "".join(args)
    for x in kwargs:
        if x in new_string:
            new_string = new_string.replace(x, kwargs[x])

    return new_string


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
