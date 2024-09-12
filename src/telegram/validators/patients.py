"""
Desc: Patient form validators
"""

import datetime

from aiogram_forms.errors import ValidationError


def age_validator(value: str):
    """
    Validated age

    ...

    Parameters
    ----------
    value : string
        A date string
    """
    try:
        date = datetime.datetime.strptime(value, "%d.%m.%Y")
    except ValueError as e:
        raise ValidationError("Date should be like: dd.mm.yyyy", "AGE") from e
    today = datetime.date.today()
    if (today - date.date()).days > 100*365:
        raise ValidationError("Patient is too old.", "AGE")
