from functools import reduce


def operate(symbol, *args):
    # return reduce(lambda x, y: eval(f"{x}{symbol}{y}"), args)
    if symbol == "+":
        return sum(args)
    elif symbol == "-":
        result = args[0]
        for x in args[1:]:
            result -= x
        return result
    elif symbol == "/":
        result = args[0]
        # result = reduce(lambda one, two: one / two, args)
        # result = [result := result / x for x in args][-1]
        for x in args[1:]:
            result /= x
        return result

    elif symbol == "*":
        # result = reduce(lambda multi, x: multi * x, args)
        result = 1
        for x in args:
            result *= x
        return result


print(operate("+", 1, 2, 3))


