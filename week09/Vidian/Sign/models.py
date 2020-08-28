from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=10)


class Book(models.Model):
    name = models.CharField(max_length=10)
    author = models.CharField(max_length=10)
    desciption = models.CharField(max_length=10, default="简爱")
