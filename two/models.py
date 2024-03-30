from django.db import models

# Create your models here.

class Feature(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=100)
