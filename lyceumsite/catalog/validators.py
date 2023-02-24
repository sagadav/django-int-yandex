import re

from django.forms import ValidationError


def validate_text(value):
    if not re.search(r"(^|[.\s])(превосходно|роскошно)($|[\s\.,;!?:])", value, re.IGNORECASE):
        raise ValidationError(
            f"{value} должна содержать слово 'превосходно' или 'роскошно'"
        )
