from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request,user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
       
                
            
    elif request.method == 'GET':
        login_form = AuthenticationForm()

    return render(request, 'views/login.html',{'login_form': login_form})            

def register(request):
    return render(request, 'views/register.html')  # Add this line

def logout(request):
    auth_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')