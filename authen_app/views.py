from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def index(request):
    return render(request, 'authen_app/index.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, ('Successfully Logged In.'))
            return redirect("Home")
        else:
            messages.success(request, ("Error Logging In"))
            return redirect("Login")
    else:
        return render(request, 'authen_app/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ('Successfully logged out'))
    return redirect("Home")

def signup_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('Successfully Signed Up'))
            return redirect('Home')

    else:
        form = SignUpForm()

    return render(request, 'authen_app/signup.html', {'form': form})
