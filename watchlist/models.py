from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class Watchlist(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.CharField(max_length=300)
    platform = models.ForeignKey(
        StreamPlatform,
        on_delete=models.CASCADE,
        related_name="watchlist",
    )
    is_fully_released = models.BooleanField(default=True)
    watch_status = models.CharField(max_length=100, default="YET_TO_START")
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    description = models.CharField(max_length=200, null=True)
    watchlist = models.ForeignKey(
        Watchlist,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rating} - {self.watchlist.title}"
