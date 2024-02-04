def team_lineup(*players):
    dictionary = {}

    for key_value in players:
        if key_value[1] not in dictionary.keys():
            dictionary[key_value[1]] = []
        dictionary[key_value[1]].append(key_value[0])

    dictionary = dict(sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0])))
    result_string = ""
    for country, player in dictionary.items():
        result_string += f"{country}:\n"
        for member in player:
            result_string += f"  -{member}\n"

    return result_string


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))


