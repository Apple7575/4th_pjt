from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField()
    description = models.TextField()
    director = models.CharField()
