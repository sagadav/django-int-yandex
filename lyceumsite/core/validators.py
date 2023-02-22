import re

from django.forms import ValidationError


def validate_slug(value):
    if re.search(r"[^a-z\d\-_]", value, re.IGNORECASE):
        raise ValidationError("Только цифры, буквы латиницы и символы - и _")
