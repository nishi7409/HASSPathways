import csv
import os
import time
import json
from django.db import models
from django.core import serializers
from django.contrib.postgres.fields import ArrayField
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Pathway(models.Model):
    pathName = models.CharField(max_length=150)
    pathDescript = models.TextField(default = 'description')
    priority1 = models.ManyToManyField('Course', related_name='priority1')
    priority2 = models.ManyToManyField('Course', related_name='priority2')
    priority3 = models.ManyToManyField('Course', related_name='priority3')

    def __str__(self):
        return self.pathName

# Individual class model
class Course(models.Model):
    prefix = models.CharField(max_length=10)
    ID = models.IntegerField(null=False, blank=False)
    name = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    HI = models.IntegerField(null=False, blank=False, default=0)
    CI = models.IntegerField(null=False, blank=False, default=0)
    DI = models.IntegerField(null=False, blank=False, default=0)
    major_retrictive = models.IntegerField(null=False, blank=False, default=0)
    fall = models.IntegerField(null=False, blank=False, default=0)
    spring = models.IntegerField(null=False, blank=False, default=0)
    summer = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.name

def parse():
    # Get the absolute csv file
    csvFile = os.getcwd() + "/" + "HassPathways.csv"

    # Open the file
    with open(csvFile, 'r') as file:
        # Read it and note the delimeter
        file_r = csv.reader(file, delimiter=',')

        # Loop through the columns
        for col in file_r:
            
            # Skip the empty empty data (work on more debugging so we can handle errors, or maybe create a Google app script that handles the errors for us... more details on that later)
            if (col[0] == "" or col[6] == "" or col[1] == "ID"):
                continue
            
            pathwayName = col[11].strip().title()
            pathResult = Pathway.objects.filter(pathName = pathwayName)
            courseResult = Course.objects.filter(prefix = col[0].strip(), ID = col[1].strip() ,name = col[2].strip().title())
            
            # Does pathway exist
            if (len(pathResult) == 0):
                tmpPath = Pathway.objects.create(pathName = pathwayName, pathDescript = col[11].strip())

                # Does course exist
                if (len(courseResult) == 0):
                    tmpCourse = Course.objects.create(
                        prefix = col[0].strip(),
                        ID = col[1].strip(),
                        name = col[2].strip().title(),
                        description = col[3].strip(),
                        HI = col[4].strip(),
                        CI = col[5].strip(),
                        DI = col[6].strip(),
                        major_retrictive = col[7].strip(),
                        fall = col[8].strip(),
                        spring = col[9].strip(),
                        summer = col[10].strip())

                    tmpCourse.save()
                    if (col[13].strip().find('1') != -1):
                        tmpPath.priority1.add(tmpCourse)
                    if (col[13].strip().find('2') != -1):
                        tmpPath.priority2.add(tmpCourse)
                    if (col[13].strip().find('3') != -1):
                        tmpPath.priority3.add(tmpCourse)
                    
                    tmpPath.save()

                else:
                    if (col[13].strip().find('1') != -1):
                        tmpPath.priority1.add(Course.objects.get(prefix = col[0].strip(), ID = col[1].strip() ,name = col[2].strip().title()))
                    if (col[13].strip().find('2') != -1):
                        tmpPath.priority2.add(Course.objects.get(prefix = col[0].strip(), ID = col[1].strip() ,name = col[2].strip().title()))
                    if (col[13].strip().find('3') != -1):
                        tmpPath.priority3.add(Course.objects.get(prefix = col[0].strip(), ID = col[1].strip() ,name = col[2].strip().title()))

                    tmpPath.save()

            else:
                tmpPath = Pathway.objects.get(pathName = pathwayName)

                # Does course exist
                if (len(courseResult) == 0):
                    tmpCourse = Course.objects.create(
                        prefix = col[0].strip(),
                        ID = col[1].strip(),
                        name = col[2].strip().title(),
                        description = col[3].strip(),
                        HI = col[4].strip(),
                        CI = col[5].strip(),
                        DI = col[6].strip(),
                        major_retrictive = col[7].strip(),
                        fall = col[8].strip(),
                        spring = col[9].strip(),
                        summer = col[10].strip())

                    tmpCourse.save()
                    if (col[13].strip().find('1') != -1):
                        tmpPath.priority1.add(tmpCourse)
                    if (col[13].strip().find('2') != -1):
                        tmpPath.priority2.add(tmpCourse)
                    if (col[13].strip().find('3') != -1):
                        tmpPath.priority3.add(tmpCourse)
                    tmpPath.save()

                else:
                    if (col[13].strip().find('1') != -1):
                        tmpPath.priority1.add(Course.objects.get(prefix = col[0].strip(), ID = col[1].strip() ,name = col[2].strip().title()))
                    if (col[13].strip().find('2') != -1):
                        tmpPath.priority2.add(Course.objects.get(prefix = col[0].strip(), ID = col[1].strip() ,name = col[2].strip().title()))
                    if (col[13].strip().find('3') != -1):
                        tmpPath.priority3.add(Course.objects.get(prefix = col[0].strip(), ID = col[1].strip() ,name = col[2].strip().title()))

                    tmpPath.save()


#Main code start
# parse()




