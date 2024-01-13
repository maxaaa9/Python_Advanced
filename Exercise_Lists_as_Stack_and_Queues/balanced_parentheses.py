from collections import deque

sequence_of_parentheses = deque(input())
open_parentheses = deque()

while sequence_of_parentheses:
    bracket = sequence_of_parentheses.popleft()

    if bracket in "{([":
        open_parentheses.append(bracket)

    elif not open_parentheses:
        print("NO")
        break

    else:
        if not open_parentheses.pop() + bracket in "{}()[]":
            print("NO")
            break

else:
    print("YES")

