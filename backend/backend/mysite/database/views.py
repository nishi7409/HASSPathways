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
import json
import requests
import os

def course(request):
    data = Course.objects.all()
    data = serializers.serialize("json", data)
    # return(request, '')
    return HttpResponse(data)

def pathway(request):
    data = Pathway.objects.all()
    data = serializers.serialize("json", data)
    return HttpResponse(data)
