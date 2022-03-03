import imp
from unicodedata import name
from django.db import models
from rest_framework import serializers
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()

    city = models.CharField(max_length=100)

     
