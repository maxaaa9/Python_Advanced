def perimeter(p_length, p_width):
    return 2 * (p_length + p_width)


def area(a_length, a_width):
    return a_length * a_width


def rectangle(length, width):
    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    return f"Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}"


print(rectangle(2, 10))


