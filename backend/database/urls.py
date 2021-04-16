from django.urls import path

from . import views

urlpatterns = [
    path('courses', views.course, name='course'),
    path('pathways', views.pathway, name='pathway')
]
