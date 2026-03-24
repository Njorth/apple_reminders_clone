from django.contrib import admin
from django.db.models import Count
from django.http import HttpRequest

from .models import List, Reminder


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ["name", "reminder_count", "colour"]

    def get_queryset(self, request: HttpRequest):
        qs = super().get_queryset(request)
        return qs.annotate(_reminder_count=Count("reminders"))

    def reminder_count(self, obj):
        return obj._reminder_count


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ["title", "list", "position"]
