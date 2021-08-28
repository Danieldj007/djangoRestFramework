from django.db import models

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=70, default='', blank= False)
    description = models.CharField(max_length=200, default='', blank= False)
    published = models.BooleanField(default=False)