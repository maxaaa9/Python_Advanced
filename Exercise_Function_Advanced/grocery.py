def grocery_store(**kwargs):
    result = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    return "\n".join(f"{part}: {quantity}" for part, quantity in result)