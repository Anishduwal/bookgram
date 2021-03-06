from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
