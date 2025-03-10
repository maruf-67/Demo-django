from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request,user)
                return render(request, 'views/register.html')
            else:
                return render(request, 'views/login.html', {'login_form': login_form})
            
    elif request.method == 'GET':
        login_form = AuthenticationForm()
        return render(request, 'views/login.html',{'login_form': login_form})            

def register(request):
    return render(request, 'views/register.html')  # Add this line