import re

from transliterate import translit


def normalize_name(name):
    return re.sub(
        r"[^a-zа-яеё]", "", translit(name.lower(), "ru", reversed=True)
    )
