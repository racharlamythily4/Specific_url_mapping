from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<h1>This is my second app of specific url mapping project')

def second(request):
    return HttpResponse('<h1>This is my second-second app of specific url mapping project</h1>')