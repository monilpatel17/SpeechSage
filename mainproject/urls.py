from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('process_speech/', views.process_speech, name = "process_speech"),
    path('howToUse/', views.howToUse, name = "howToUse"),
    path('home/', views.index, name="index"),
    path('resource/', views.resource, name ="resource"),
]
