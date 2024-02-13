def accommodate_new_pets(capacity: int, max_weight_per_pet: float, *data):
    my_pets = {}
    pet_list = data

    all_accommodate = True
    for pet, weight in pet_list:
        if capacity <= 0:
            all_accommodate = False
            break

        if capacity and weight <= max_weight_per_pet:
            if pet not in my_pets.keys():
                my_pets[pet] = 0
            my_pets[pet] += 1
            capacity -= 1

    my_return_string = ""
    if all_accommodate:
        my_return_string += f"All pets are accommodated! Available capacity: {capacity}.\n"
    else:
        my_return_string += "You did not manage to accommodate all pets!\n"

    my_pets = dict(sorted(my_pets.items(), key=lambda x: x[0]))
    my_return_string += "Accommodated pets:\n"
    for pet, quantity in my_pets.items():
        my_return_string += f"{pet}: {quantity}\n"

    return my_return_string.rstrip()


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
