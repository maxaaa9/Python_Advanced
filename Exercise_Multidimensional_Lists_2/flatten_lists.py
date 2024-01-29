input_string = input().split("|")

new_string = []
for x in input_string[::-1]:
    new_string.extend(x.split())

print(*new_string)
