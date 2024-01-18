from functools import reduce

string_sequence = input().split()

index = 0

operation = {
    "+": lambda d: reduce(lambda one, two: one + two, map(int, string_sequence[:index])),
    "-": lambda d: reduce(lambda one, two: one - two, map(int, string_sequence[:index])),
    "*": lambda d: reduce(lambda one, two: one * two, map(int, string_sequence[:index])),
    "/": lambda d: reduce(lambda one, two: one // two, map(int, string_sequence[:index])),
}

while index < len(string_sequence):
    element = string_sequence[index]

    if element in "+-*/":
        string_sequence[0] = operation[element](index)
        [string_sequence.pop(1) for _ in range(index)]
        index = 1

    index += 1

print(*string_sequence)