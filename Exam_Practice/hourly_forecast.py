def forecast(*args):
    my_data = {}
    for city, weather in args:
        my_data[city] = weather

    sorter = {
        "Sunny": 1,
        "Cloudy": 2,
        "Rainy": 3,
    }

    sorted_data = dict(sorted(my_data.items(), key=lambda x: (sorter[x[1]], x[0])))
    return_string = ""
    for city, weather in sorted_data.items():
        return_string += f"{city} - {weather}\n"

    return return_string


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))