from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required


def login(request):
    if request.user.is_authenticated:
        return redirect('index')  # Redirect if already logged in
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

        # else:
        #     messages.error(request, "Invalid username or password.")

    elif request.method == 'GET':
        login_form = AuthenticationForm()

    return render(request, 'views/login.html',{'login_form': login_form})

def register(request):
    if request.user.is_authenticated:
        return redirect('index')  # Redirect if already logged in
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db() # load the profile instance created by the signal
            username = register_form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Please correct the error below.")

    elif request.method == 'GET':
        register_form = UserCreationForm()

    return render(request, 'views/register.html', {'register_form': register_form})

@login_required
def logout(request):
    auth_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')

class RegisterView(View):

    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'views/register.html',{'register_form': register_form})

    def post(self, request):
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            auth_login(request, user)
            return redirect('index')
        return render(request, 'views/register.html',{'register_form': register_form})
