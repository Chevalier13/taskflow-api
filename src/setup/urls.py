from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "TaskFlow API em Django funcionando no Docker!"})

urlpatterns = [
    path('', home),  
]