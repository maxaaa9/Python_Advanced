reservation_codes_data = set()

number_of_reservation = int(input())

for _ in range(number_of_reservation):
    reservation_code = input()
    if len(reservation_code) == 8:
        reservation_codes_data.add(reservation_code)

arrived_guest = input()
while arrived_guest != "END":
    if arrived_guest in reservation_codes_data:
        reservation_codes_data.remove(arrived_guest)
    arrived_guest = input()

else:
    print(len(reservation_codes_data))
    for code in sorted(reservation_codes_data):
        print(code)
