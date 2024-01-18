from collections import deque

string_sequence = deque(input().split())

index = 0

while len(string_sequence) > 1:
    element = string_sequence[index]
    if element == "+":
        for _ in range(index - 1):
            string_sequence.appendleft(int(string_sequence.popleft()) + int(string_sequence.popleft()))
    elif element == "-":
        for _ in range(index - 1):
            string_sequence.appendleft(int(string_sequence.popleft()) - int(string_sequence.popleft()))
    elif element == "*":
        for _ in range(index - 1):
            string_sequence.appendleft(int(string_sequence.popleft()) * int(string_sequence.popleft()))
    elif element == "/":
        for _ in range(index - 1):
            string_sequence.appendleft(int(string_sequence.popleft()) // int(string_sequence.popleft()))
    if element in "+-*/":
        del string_sequence[1]
        index = 1

    index += 1

print(string_sequence[0])

