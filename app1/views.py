from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<h1>My first Specific url mapping project</h1>')

def second(request):
    return HttpResponse('<h1>This is my first-second specific url mapping project')