def add_songs(*info):
    my_lyrics = {}

    for name, data in info:
        if name not in my_lyrics.keys():
            my_lyrics[name] = []
        for text in data:
            my_lyrics[name].append(f"{text}")

    my_return = ""
    for name, lyrics in my_lyrics.items():
        my_return += f"- {name}\n"
        for rows in lyrics:
            my_return += f"{rows}\n"

    return my_return



print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))