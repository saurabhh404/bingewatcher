# Generated by Django 5.0.4 on 2024-05-06 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StreamPlatform",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("about", models.CharField(default="", max_length=150)),
                ("website", models.CharField(default="", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Watchlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("storyline", models.CharField(max_length=300)),
                ("is_fully_released", models.BooleanField(default=True)),
                (
                    "watch_status",
                    models.CharField(default="YET_TO_START", max_length=100),
                ),
                ("added", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Movie",
        ),
    ]