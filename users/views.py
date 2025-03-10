from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.shortcuts import redirect


def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('index')
            else:
                pass
            
    elif request.method == 'GET':
        login_form = AuthenticationForm()
        return render(request, 'views/login.html',{'login_form': login_form})            

def register(request):
    return render(request, 'views/register.html')  # Add this line

def logout(request):
    auth_logout(request)
    return redirect('index')