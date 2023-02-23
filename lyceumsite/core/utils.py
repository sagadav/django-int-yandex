import re


def normalize_name(name):
    cyr_to_eng = str.maketrans(
        {
            "а": "a",
            "е": "e",
            "у": "y",
            "х": "x",
            "р": "p",
            "с": "c",
            "о": "o",
            "к": "k",
            "г": "r",
        }
    )
    return re.sub(r"[^a-zа-яеё]", "", name.lower().translate(cyr_to_eng))

