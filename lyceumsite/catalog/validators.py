from django.forms import ValidationError


def validate_text(value):
    if "превосходно" not in value and "роскошно" not in value:
        raise ValidationError(
            f"{value} должна содержать слово 'превосходно' или 'роскошно'"
        )
