import typing as _tp

from django.db import models
from django.core.exceptions import ValidationError
from django.forms.fields import Textarea

import dateutil.rrule as _rrule


def _parse_rrule_or_none(value: _tp.Optional[str]) -> _tp.Optional[_rrule.rrule]:
    if value is None:
        return None

    try:
        rrule = _rrule.rrulestr(value)
    except (ValueError, TypeError) as e:
        raise ValidationError("Invalid rrule string.") from e
    return rrule


class RruleField(models.TextField):

    description = "A date recurrence rule"

    def from_db_value(self, value: _tp.Optional[str], expression, connection) -> _tp.Optional[_rrule.rrule]:
        return _parse_rrule_or_none(value)

    def to_python(self, value: _tp.Optional[_tp.Union[_rrule.rrule, str]]) -> _tp.Optional[_rrule.rrule]:
        if isinstance(value, _rrule.rrule):
            return value

        return _parse_rrule_or_none(value)

    def get_prep_value(self, value: _rrule.rrule) -> str:
        return str(value)

    def value_to_string(self, obj) -> str:
        value = self.value_from_object(obj)
        return self.get_prep_value(value)
