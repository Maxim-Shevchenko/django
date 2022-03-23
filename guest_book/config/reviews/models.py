from django.db import models
class Review(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    rating = models.IntegerField()
    review = models.TextField()
# Create your models here.
