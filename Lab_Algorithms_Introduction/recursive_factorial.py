def recursive_factorial(num):
    if num == 1:
        return num
    return num * recursive_factorial(num - 1)


print(recursive_factorial(int(input())))
