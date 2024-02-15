from collections import deque

seats = input().split(", ")
first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = deque([int(x) for x in input().split(", ")])
matched_seats = []
total_rotations = 0

while total_rotations != 10 and len(matched_seats) != 3:
    digit_one = first_sequence.popleft()
    digit_two = second_sequence.pop()
    ascii_sum = chr(digit_one + digit_two)
    total_rotations += 1

    if str(digit_one) + ascii_sum in seats:
        if str(digit_one) + ascii_sum not in matched_seats:
            matched_seats.append(str(digit_one) + ascii_sum)

    elif str(digit_two) + ascii_sum in seats:
        if str(digit_two) + ascii_sum not in matched_seats:
            matched_seats.append(str(digit_two) + ascii_sum)

    else:
        first_sequence.append(digit_one)
        second_sequence.appendleft(digit_two)

print(f"Seat matches: {', '.join(matched_seats)}")
print(f"Rotations count: {total_rotations}")