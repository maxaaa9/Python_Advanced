def cookbook(*data):
    my_recipe = {}
    for food, country, recipe in data:
        if country not in my_recipe.keys():
            my_recipe[country] = []
        my_recipe[country].append([food, recipe])
    my_recipe = dict(sorted(my_recipe.items(), key=lambda x: (-len(x[1]), x[0])))
    my_string = ""
    for cuisine, recipes in my_recipe.items():
        my_string += f"{cuisine} cuisine contains {len(my_recipe[cuisine])} recipes:\n"
        for food, elements in sorted(recipes):
            my_string += f"  * {food} -> Ingredients: {', '.join(elements)}\n"

    return my_string


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))