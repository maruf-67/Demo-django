from django.shortcuts import render


def login(request):
    return render(request, 'views/login.html')  # Add this line

def register(request):
    return render(request, 'views/register.html')  # Add this line