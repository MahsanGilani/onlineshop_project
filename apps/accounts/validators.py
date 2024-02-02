from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels

def validate_birthday(value):
    if value and value > jmodels.jDate.today():
        raise ValidationError(
            _('%(value)s is not a valid date. It must be in the past.'),
            params={'value': value},
        )