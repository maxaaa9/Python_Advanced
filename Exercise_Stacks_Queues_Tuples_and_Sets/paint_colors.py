from collections import deque

my_string = deque(input().split())

all_colors = {"red", "yellow", "blue", "orange", "purple", "green"}
receipt = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

my_colors = []
while my_string:
    left_substring = my_string.popleft() if my_string else ""
    right_substring = my_string.pop() if my_string else ""
    mixed_color = left_substring + right_substring
    for color in (left_substring + right_substring, right_substring + left_substring):
        if color in all_colors:
            mixed_color = color
            break
    if mixed_color in all_colors:
        my_colors.append(mixed_color)

    else:
        string_middle = len(my_string) // 2
        left_cut = left_substring[:- 1]
        right_cut = right_substring[:- 1]
        for cut in (left_cut, right_cut):
            if cut:
                my_string.insert(string_middle, cut)

for colors in set(receipt.keys()).intersection(my_colors):
    if not receipt[colors].issubset(my_colors):
        my_colors.remove(colors)
print(my_colors)
