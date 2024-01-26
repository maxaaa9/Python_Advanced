def recursive_power(*args):
    number = args[0]
    power = args[1]
    if power == 0:
        return 1
    return number * recursive_power(number, power - 1)

print(recursive_power(10, 100))
