text = input()
parentheses = []

for idx in range(len(text)):
    if text[idx] == "(":
        parentheses.append(idx)
    elif text[idx] == ")":
        start_index = parentheses.pop()
        print(text[start_index:idx + 1])
