from django.db import models
from django.conf import *
from time import *

# Create your models here.

class post(models.Model):
    
    title=models.CharField(max_length=20)
    text=models.TextField()
    date=models.DateTimeField()

    def __str__(self):
        return self.title
    
    def date__now(self):
        self.date=timezone.now()
        self.save()

    
    