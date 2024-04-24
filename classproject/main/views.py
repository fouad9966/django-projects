from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('<h1 Hello World />')
    return render(request, 'index.html')

def greeting(request):
    return render(request, 'greeting.html')

