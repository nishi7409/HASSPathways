from django.shortcuts import render
from django.http import HttpResponse
from api.models import Course
from api.models import Pathway
# this is where the functions that fire when the users request things

def home(request):
	# this should load up the basic homepage with all the data for all classes and pathways


	return render(request,"index.html", Pathway.objects.all())

def about(request):
	#return HttpResponse('about')
	return render(request,"api/aboutpage.html")

	#https://docs.google.com/document/d/1P12Jiir5qdBkm9TWuAv1ruS_NNHkPaFyZMzD6FOe1fs/edit?usp=sharing
	
