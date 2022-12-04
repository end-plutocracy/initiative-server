import datetime as _dt

import dateutil.rrule as _rrule
from django.contrib.auth.models import User
from django.db import models

from . import fields as _fields


# Create your models here.


class Attendance(models.Model):
    signee: "Signee" = models.OneToOneField(
        "Signee", on_delete=models.CASCADE, related_name="attendance"
    )

    def __str__(self):
        return f"Attendance of {self.signee.user.username}"


class RecurrenceRule(models.Model):
    attendance: Attendance = models.ForeignKey(
        Attendance, on_delete=models.CASCADE, related_name="recurrence_rules"
    )
    recurrence_rule: _rrule.rrule = _fields.RruleField(max_length=2048)
    is_positive: bool = models.BooleanField()

    def __str__(self):
        prefix = "+" if self.is_positive else "-"
        return f"{prefix}({self.recurrence_rule})"


class DateTime(models.Model):
    attendance: Attendance = models.ForeignKey(
        Attendance, on_delete=models.CASCADE, related_name="date_times"
    )
    datetime: _dt.datetime = models.DateTimeField()
    is_positive: bool = models.BooleanField()

    def __str__(self):
        return f"{'including' if self.is_positive else 'excluding'} {self.datetime.isoformat()}"


class Initiative(models.Model):
    title: str = models.CharField(max_length=2048)
    description: str = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    stopped_accepting_signatures_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Manager(models.Model):
    user: User = models.ForeignKey(User, on_delete=models.CASCADE)
    initiative: Initiative = models.ForeignKey(
        Initiative, on_delete=models.CASCADE, related_name="managers"
    )

    def __str__(self):
        return f"Manager {self.user.username} for {self.initiative.title}"


class Signature(models.Model):
    signee: "Signee" = models.ForeignKey(
        "Signee", on_delete=models.CASCADE, related_name="signatures"
    )
    initiative: Initiative = models.ForeignKey(
        Initiative, on_delete=models.CASCADE, related_name="signatures"
    )
    signed_on: _dt.datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        text = f"{self.signee.user.username} signed {self.initiative.title} on {self.signed_on.isoformat()}"
        return text


class Collector(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Collector {self.user.username}"


class CollectedSignature(models.Model):
    collected_on: _dt.datetime = models.DateTimeField(auto_now=True)
    collector: "Collector" = models.ForeignKey(
        Collector, null=True, on_delete=models.SET_NULL, related_name="signatures"
    )
    signature: Signature = models.OneToOneField(
        Signature, on_delete=models.PROTECT, related_name="collected_signature"
    )

    def __str__(self):
        text = f"{self.collector.user.username} collected  signature on {self.collected_on.isoformat()}"
        return text


class Signee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Signee {self.user.username}"
