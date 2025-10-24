from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    duration_min = models.IntegerField()
    director = models.CharField(max_length=100)
    description = models.TextField()
    premiere = models.DateTimeField()
    age_rating = models.IntegerField()

