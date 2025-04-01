from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'caption':"airplanes"
    }
    return render(request,  'main/index.html', data)

def new(request):
    return render(request,  'main/new.html')

def page3(request):
    return render(request, 'main/page3.html')

def page4(request):
    return render(request, 'main/page4.html')