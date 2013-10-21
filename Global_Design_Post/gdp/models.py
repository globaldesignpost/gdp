
from django.db import models

# Create your models here.


class Feed(models.Model):
    title = models.CharField(max_length=30)
    Description = models.CharField(max_length=40)
    URL = models.CharField(max_length=30)
    type = models.CharField(max_length=30)