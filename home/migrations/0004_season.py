# Generated by Django 2.2.16 on 2020-09-03 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_podcaster"),
    ]

    operations = [
        migrations.CreateModel(
            name="Season",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("season_number", models.PositiveIntegerField()),
                ("season_description", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="season_user",
                        to="home.Podcaster",
                    ),
                ),
            ],
        ),
    ]