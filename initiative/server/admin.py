from django.contrib import admin

from . import models as _models

# Register your models here.


class RecurrenceInline(admin.StackedInline):
    model = _models.RecurrenceRule
    extra = 1


class DateTimeInline(admin.StackedInline):
    model = _models.DateTime
    extra = 1


class AttendanceAdmin(admin.ModelAdmin):
    inlines = [RecurrenceInline, DateTimeInline]


class SignatureInline(admin.StackedInline):
    model = _models.Signature
    extra = 5


class AttendanceInline(admin.StackedInline):
    model = _models.Attendance
    extra = 1


class SigneeAdmin(admin.ModelAdmin):
    inlines = [SignatureInline, AttendanceInline]


class CollectedSignatureInline(admin.StackedInline):
    model = _models.CollectedSignature


class CollectorAdmin(admin.ModelAdmin):
    inlines = [CollectedSignatureInline]


admin.site.register(_models.Signee, SigneeAdmin)
admin.site.register(_models.Collector, CollectorAdmin)
admin.site.register(_models.Manager)
admin.site.register(_models.Attendance, AttendanceAdmin)
admin.site.register(_models.Initiative)




