from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Series(models.Model):
    name = models.CharField(max_length=100)
    tags = models.CharField(max_length=500)
    is_watched = models.BooleanField(default=False)
    ott = models.CharField(max_length=100, default="unknown")

    def __str__(self):
        return self.name
