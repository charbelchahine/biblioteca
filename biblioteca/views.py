from django.shortcuts import render
from django.http import HttpResponse

helloWorld = "Hello, world. Welcome to Biblioteca. My creators are:"
nomaan = "Nomaan"

def index(request):
    return HttpResponse(helloWorld + " <br> " 
    + nomaan)
