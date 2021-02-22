import csv
import os
import time
import json
from django.db import models
from django.core import serializers
from django.contrib.postgres.fields import ArrayField

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
    pathways = ArrayField(models.CharField(max_length=150, blank=True), default=list, size=10, null=True, blank=True)

    def __str__(self):
        return self.name

def parse():
    # Get the absolute csv file
    csvFile = os.getcwd() + "/" + "HassPathways_SMALL.csv"

    # Open the file
    with open(csvFile, 'r') as file:
        # Read it and note the delimeter
        file_r = csv.reader(file, delimiter=',')

        # Loop through teh columns
        for col in file_r:
            
            # Skip the empty empty data (work on more debugging so we can handle errors, or maybe create a Google app script that handles the errors for us... more details on that later)
            if (col[0] == "" or col[6] == "" or col[1] == "ID"):
                continue

            # Make sure the class object doesn't already exist
            if (len(Course.objects.filter(prefix = col[0].strip(), ID = col[1].strip() ,name = col[2].strip().lower())) == 0):
                if (col[2].strip() == "AI and Society"):
                    print("Creating " + col[2].strip())
                # Create class
                created = Course.objects.create(
                prefix = col[0].strip(),
                ID = col[1].strip(),
                name = col[2].strip(),
                description = col[3].strip(),
                HI = col[4].strip(),
                CI = col[5].strip(),
                DI = col[6].strip(),
                fall = col[7].strip(),
                spring = col[8].strip(),
                summer = col[9].strip())

                created.pathways.append(col[10].strip().lower())

                # Save class
                created.save()

            else:
                if (col[2].strip().lower() == "AI and Society"):
                    print("Adding to it" + col[2].strip())
                result = Course.objects.get(prefix__exact = col[0].strip(), ID__exact = col[1].strip() ,name__exact = col[2].strip().lower())
                if (col[10].strip().lower() in result.pathways):
                    continue
                else:
                    result.pathways.append(col[10].strip().lower())
                    result.save()
                
def writeJson():
    data = serializers.serialize("json", Course.objects.all())
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


#Main code start
parse()
writeJson()
print("Done!")

# HASSPathways.csv
