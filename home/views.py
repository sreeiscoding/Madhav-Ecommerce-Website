from django.shortcuts import render

def index(request):
    return render(request, "home/index.html") 

def navbar(request):
    return render(request, "home/navbar.html") 
