# Write a program that reads a string with N integers from the console,
#   separated by a single space, and reverses them using a stack.
# Print the reversed integers on one line, separated by a single space.

input_numbers = input().split()
output_numbers = []

while input_numbers:
    output_numbers.append(input_numbers.pop())

print(" ".join(output_numbers))
