from django.db import models

# Create your models here.


class RouletteUser(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    money = models.FloatField()
    username = models.EmailField()
    photo = models.ImageField(upload_to='images')
