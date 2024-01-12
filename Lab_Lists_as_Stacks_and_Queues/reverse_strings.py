input_string = list(input())
stack = []
for reverse in range(len(input_string)):
    stack.append(input_string.pop())

print("".join(stack))

