sequence_one = set(map(int, input().split()))
sequence_two = set(map(int, input().split()))

for _ in range(int(input())):

    command, stage, *data = input().split()

    if command + " " + stage == "Add First":
        sequence_one = sequence_one.union(int(x) for x in data)
    elif command + " " + stage == "Add Second":
        sequence_two = sequence_two.union(int(x) for x in data)
    elif command + " " + stage == "Remove First":
        sequence_one = sequence_one.difference(int(x) for x in data)
    elif command + " " + stage == "Remove Second":
        sequence_two = sequence_two.difference(int(x) for x in data)
    elif command + " " + stage == "Check Subset":
        print(sequence_two.issubset(sequence_one))

print(*sorted(sequence_one), sep=", ")
print(*sorted(sequence_two), sep=", ")
