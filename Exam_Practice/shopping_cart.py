def shopping_cart(*foods):
    meal = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2,
    }

    shopping_dict = {
        "Soup": [],
        "Pizza": [],
        "Dessert": [],
    }

    empty_cart = True
    for data in foods:
        if data == "Stop":
            break

        food = data[0]
        element = data[1]

        if len(shopping_dict[food]) < meal[food] and element not in shopping_dict[food]:
            shopping_dict[food].append(element)
            empty_cart = False

    if empty_cart:
        return "No products in the cart!"

    shopping_dict = dict(sorted(shopping_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    my_output = ""
    for meals, el in shopping_dict.items():
        my_output += f"{meals}:\n"
        for element in sorted(el):
            my_output += f" - {element}\n"

    return my_output


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))