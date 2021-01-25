import csv
import os
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
    pathway = models.TextField(null=False, blank=False)

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
            if (len(Class.objects.filter(prefix = col[0].strip(), name = col[2].strip())) == 0):
                # Create class
                created = Class(
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
            

parse()
print("Done!")

# HASSPathways.csv
