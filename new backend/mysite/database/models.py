import csv
import os
import time
import json
from django.db import models
from django.core import serializers
from django.contrib.postgres.fields import ArrayField

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Pathway(models.Model):
    pathName = models.CharField(max_length=150, blank = True)
    relatedCourses = models.ManyToManyField('Course')

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
    fall = models.IntegerField(null=False, blank=False, default=0)
    spring = models.IntegerField(null=False, blank=False, default=0)
    summer = models.IntegerField(null=False, blank=False, default=0)
    pathwaysArray = ArrayField(models.CharField(max_length=150, blank=True), default=list, size=10, null=True, blank=True)

    def __str__(self):
        return self.name

def parse():
    # Get the absolute csv file
    csvFile = os.getcwd() + "/" + "HassPathways_SMALL.csv"

    # Open the file
    with open(csvFile, 'r') as file:
        # Read it and note the delimeter
        file_r = csv.reader(file, delimiter=',')

        # Loop through the columns
        for col in file_r:
            
            # Skip the empty empty data (work on more debugging so we can handle errors, or maybe create a Google app script that handles the errors for us... more details on that later)
            if (col[0] == "" or col[6] == "" or col[1] == "ID"):
                continue
            
            # Since we know we are on an actual line grab the specified course/pathway if it exists
            courseResult = Course.objects.filter(prefix = col[0].strip(), ID = col[1].strip() ,name = col[2].strip().lower())
            pathwayName = col[10].strip().lower()
            pathResult = Pathway.objects.filter(pathName = pathwayName)
            flag = False

            # Checker to see if the path exists or not
            if (len(pathResult) != 0):
                flag = True

            # Check if the course already exists in the database or not
            if (len(courseResult) == 0):
                # Create class
                created = Course.objects.create(
                prefix = col[0].strip(),
                ID = col[1].strip(),
                name = col[2].strip().lower(),
                description = col[3].strip(),
                HI = col[4].strip(),
                CI = col[5].strip(),
                DI = col[6].strip(),
                fall = col[7].strip(),
                spring = col[8].strip(),
                summer = col[9].strip())

                created.pathwaysArray.append(pathwayName)

                # Save the course to database
                created.save()

                # Now check if the pathway exists in the database
                if (flag == False):
                    print("Creating")
                    # If it does not already exist create the pathway and make the course associated to it
                    tmp = Pathway.objects.create(pathName = pathwayName)
                    tmp.relatedCourses.add(created)

                    tmp.save()

                # If pathway already exists make the course related to it
                else:
                    print("adding to")
                    pathResult[0].relatedCourses.add(created)
                    pathResult[0].save()

            # If (Course) already exists add the pathway it is associated with
            else:

                # Need to check if the path exists, if it doesn't create
                if (flag == False):
                    tmp = Pathway.objects.create(pathName = pathwayName)
                    tmp.relatedCourses.add(courseResult[0])

                    tmp.save()
                else:
                    # If the course is already related to the pathway skip, if not add to
                    if courseResult[0] in pathResult[0].relatedCourses.all():
                        continue
                    else:
                        courseResult[0].Pathways__set.add(pathResult[0])
                        courseResult[0].save()

        
def writeJson():
    # Honestly have no idea what this doess
    data = serializers.serialize("json", Course.objects.all())
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

#Main code start
parse()
# writeJson()
# print("Done!")

# HASSPathways.csv
