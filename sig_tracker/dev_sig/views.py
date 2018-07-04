from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1> List of Topics under Development Sig</h1>''')

def detail(request, dev_id):
    return HttpResponse("<h2> Details for dev_id:" + str(dev_id) + "</h2>")
