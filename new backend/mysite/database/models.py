import csv
import os
import time
import json
from django.contrib.postgres.fields import ArrayField
from django.db import models

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Individual class model
class Class(models.Model):
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

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)

#Parse through CSV file
def parse():
    # Get the absolute csv file
    csvFile = os.getcwd() + "/" + "HassPathways.csv"

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
            if (len(Class.objects.filter(prefix = col[0].strip(), ID = col[1].strip() ,name = col[2].strip())) == 0):
                # Create class
                created = Class.objects.create(
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
                
                created.pathways.append(col[10].strip())

                # Save class
                created.save()

            else:
                result = Class.objects.get(prefix = col[0].strip(), ID = col[1].strip() ,name = col[2].strip())
                if (col[10].strip() in result.pathways):
                    continue
                else:
                    result.pathways.append(col[10].strip())
                    result.save()
                
def writeJson():
    with open('data.json', 'w', encoding='utf-8') as f:
        for course in Class.objects.all():
            json.dump(course.toJSON(), f, ensure_ascii=False)


#Main code start
parse()
writeJson()
print("Done!")

# HASSPathways.csv
