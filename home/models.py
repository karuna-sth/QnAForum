from django.db import models

# Create your models here.
class Questions(models.Model):
    topic = models.CharField(max_length=150)
    description = models.TextField()
