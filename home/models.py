from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Podcaster(models.Model):
    "Generated Model"
    name = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="podcaster_name",
    )
    podcast_name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    podcast_description = models.BigIntegerField(
        null=True,
        blank=True,
    )
    podcast_link = models.TextField(
        null=True,
        blank=True,
    )


class Season(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "home.Podcaster",
        on_delete=models.CASCADE,
        related_name="season_user",
    )
    season_number = models.PositiveIntegerField()
    season_description = models.TextField()
