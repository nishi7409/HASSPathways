from django.db import models

# Create your models here.
class Class(models.Model):
    prefix = models.CharField(max_length=5)
    ID = models.IntegerField()
    name = models.CharField()
    description = models.TextField()
    HI = models.BooleanField()
    CI = models.BooleanField()
    DI = models.BooleanField()
    fall = models.BooleanField()
    spring = models.BooleanField()
    summer = models.BooleanField()
    pathway = models.CharField()

def test():
    a = Class(prefix="", id=)
    a.save() # --> database
