from django.db import models

# Create your models here.
class Login():
    username = models.TextField()
    passwords = models.TextField()
    #price = models.IntegerField()