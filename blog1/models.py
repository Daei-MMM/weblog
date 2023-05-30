from django.db import models
from django.conf import *
from time import *
from datetime import datetime
# Create your models here.

class post(models.Model):
    
    title=models.CharField(max_length=20)
    text=models.TextField()
    date=models.DateTimeField(default=datetime.now())

class todo(models.Model):
   
    title = models.CharField(max_length=50)
    text = models.TextField()
