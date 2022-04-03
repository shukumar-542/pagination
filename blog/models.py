from django.db import models

# Create your models here.
class blog(models.Model):
      title = models.CharField(max_length=100)
      des = models.TextField(max_length=400)
      date =models.DateField()