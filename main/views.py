from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'views/index.html' , { "name" : 'Demo Work'})  # Add this line

def about(request):
    return render(request, 'views/about.html')  # Add this line

def contact(request):
    return render(request, 'views/contact.html')  # Add this line

def post(request):
    return render(request, 'views/post.html')  # Add this line
