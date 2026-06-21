# core/admin.py

from django.contrib import admin
from .models import Operator, DaySchedule


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ["name", "phone"]
    search_fields = ["name", "phone"]


@admin.register(DaySchedule)
class DayScheduleAdmin(admin.ModelAdmin):
    list_display = ["day_of_week", "operator"]
    list_select_related = ["operator"]  # ← kills the N+1 query in list view
    list_editable = ["operator"]        # ← manager edits all 7 rows inline, no clicking