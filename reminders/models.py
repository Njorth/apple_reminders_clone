from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager


class List(models.Model):
    name = models.CharField(max_length=128)

    class Colours(models.TextChoices):
        PRIMARY = "primary"
        SECONDARY = "secondary"
        SUCCESS = "success"
        INFO = "info"

    colour = models.CharField(
        max_length=12, choices=Colours.choices, default=Colours.PRIMARY
    )

    if TYPE_CHECKING:
        reminders: RelatedManager[Reminder]

    def __str__(self) -> str:
        return self.name


class Reminder(models.Model):
    title = models.CharField(max_length=128)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="reminders")
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ["position"]

    def __str__(self) -> str:
        return self.title
