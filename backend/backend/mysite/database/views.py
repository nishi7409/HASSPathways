from django.http import HttpResponse, HttpRequest, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.conf import settings
from .models import *
from django import views
from django.core import mail
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django import forms
import json as simplejson
import requests

import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Course, Pathway

def course(request):
    data = Course.objects.all()
    data = serializers.serialize("json", data)
    return HttpResponse(data)

def pathway(request):
    data = Pathway.objects.all()
    data = serializers.serialize("json", data)
    return HttpResponse(data)

@permission_required('admin.can_add_log_entry')
def _upload(request):
    template = "_upload.html"

    prompt = {
        'order': 'Order of the CSV should be prefix, ID, Name, Description, HI, CI, DI, Major restrictive, Fall, Spring, Summer, Pathway, Pathway description, Priority'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file!')

    Pathway.objects.all().delete()
    Course.objects.all().delete()
    Pathway.objects.all().delete()

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=','):
        
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

    data = Course.objects.all()
    data = serializers.serialize("json", data)
    courseDataFile = open('CourseData.json', 'w')
    courseDataFile.truncate()
    courseDataFile.write(json.dumps(json.loads(data), indent=4, sort_keys=True))
    courseDataFile.close()

    data = Pathway.objects.all()
    data = serializers.serialize("json", data)
    pathwayDataFile = open('PathwayData.json', 'w')
    pathwayDataFile.truncate()
    pathwayDataFile.write(json.dumps(json.loads(data), indent=4, sort_keys=True))
    pathwayDataFile.close()

    context = {
        'success': 'Successfully uploaded!'
    }
    return render(request, template, context)
    
