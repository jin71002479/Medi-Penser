from django.db import models

# Create your models here.
class Photo(models.Model):
    names= models.CharField(max_length=200)