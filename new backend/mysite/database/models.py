import csv

from django.db import models

# Create your models here.
class Class(models.Model):
    prefix = models.CharField(max_length=5)
    ID = models.IntegerField()
    name = models.CharField()
    description = models.TextField()
    HI = models.IntegerField()
    CI = models.IntegerField()
    DI = models.IntegerField()
    fall = models.IntegerField()
    spring = models.IntegerField()
    summer = models.IntegerField()
    pathway = models.CharField()

def parse():
    with open('HASSPathways.csv', 'r') as file:
        file_r = csv.reader(file, delimiter=',', quotechar="")

        for column in file_r:
            created = Class(
            ID = col[1],
            name = col[2],
            description = col[3],
            HI = col[4],
            CI = col[5],
            DI = col[6],
            fall = col[7],
            spring = col[8],
            summer = col[9],
            pathway = col[10])
            
            created.save() # --> database

parse()
print('Done!')