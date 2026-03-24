from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from django.db.models.manager import RelatedManager


class List(models.Model):


    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=128)

    class Colours(models.TextChoices):
        PRIMARY = "primary"
        SECONDARY = "secondary"
        SUCCESS = "success"
        INFO = "info"


    class Icons(models.TextChoices):
        LIST = "list"
        BOOKMARK = "bookmark"
        KEY = "key"
        PRESENT = "present"

    colour = models.CharField(
        max_length=12, choices=Colours.choices, default=Colours.PRIMARY
    )

    icon = models.CharField(
        max_length=24, choices=Icons.choices, default=Icons.LIST
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
