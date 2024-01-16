n_usernames = int(input())

unique_collection = set()

for name in range(n_usernames):
    unique_collection.add(input())

print(*unique_collection, sep="\n")