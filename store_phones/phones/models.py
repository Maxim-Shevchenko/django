from django.db import models
from django.contrib.auth import get_user_model
class Phone(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.title}'
# Create your models here.
