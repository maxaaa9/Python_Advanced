def sorting_cheeses(**cheeses):
    cheeses_dict = sorted(cheeses.items(), key=lambda x: (-len(x[1]), x[0]))

    return_list = []

    for name, quantity in cheeses_dict:
        quantity = sorted(quantity, reverse=True)
        return_list.append(name)
        return_list += quantity
    else:
        return "\n".join(str(x) for x in return_list)


print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)