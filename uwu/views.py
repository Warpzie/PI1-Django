from django.shortcuts import render, HttpResponse

def index(request):
    #python code
    return HttpResponse("hello world")