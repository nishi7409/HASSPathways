import csv
import os
import time
from django.db import models

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Individual class model
class Classes(models.Model):
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
    pathway = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name

class Pathways(models.Model):
    pathway_name = models.TextField(null=False, blank=False)
    #pathway_description = models.TextField(null=False, blank=False)
    courses = models.ManyToManyField(Classes)

    def __str__(self):
        return self.pathway_name

# Parse through CSV file
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
            if (len(Classes.objects.filter(prefix = col[0].strip(), name = col[2].strip())) == 0):
                # Create class
                created = Classes(
                prefix = col[0].strip(),
                ID = col[1].strip(),
                name = col[2].strip(),
                description = col[3].strip(),
                HI = col[4].strip(),
                CI = col[5].strip(),
                DI = col[6].strip(),
                fall = col[7].strip(),
                spring = col[8].strip(),
                summer = col[9].strip(),
                pathway = col[10].strip())
                
                # Save class
                created.save() # --> database
            
def makePath():
    for course in Classes.objects.all():
        if (len(Pathways.objects.filter(pathway = course.pathway) == 0)):
            created = Pathways(pathway_name = course.pathway, courses = course)
            created.save()
        
        else:
            result = Pathways.objects.get(name__icontains=course.pathway)
            result[0].courses.add(course)
            result.save()

parse()
makePath()
print("Done!")

# HASSPathways.csv
