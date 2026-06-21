
from django.db import models


class Operator(models.Model):
    """A technician with a name and a callable phone number."""

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.name} ({self.phone})"

    class Meta:
        verbose_name = "Operator"
        verbose_name_plural = "Operators"


class DaySchedule(models.Model):
    """Maps exactly one operator to exactly one day of the week."""

    DAYS = [
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    ]

    day_of_week = models.IntegerField(choices=DAYS, unique=True)
    operator = models.ForeignKey(
        Operator,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="schedules",
    )

    def __str__(self) -> str:
        return f"{self.get_day_of_week_display()} → {self.operator}"

    class Meta:
        ordering = ["day_of_week"]
        verbose_name = "Day Schedule"
        verbose_name_plural = "Weekly Schedule"