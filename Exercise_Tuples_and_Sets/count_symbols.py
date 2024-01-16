text = input()
count_set = {}


for symbol in set(text):
    count_set[symbol] = text.count(symbol)

else:
    for key, value in sorted(count_set.items()):
        print(f"{key}: {value} time/s")
