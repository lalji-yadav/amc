from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from django.contrib import messages

# Create your views here.


def authBase(request):
    return render(request, 'authbase.html')


def loginPage(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}")
                return redirect('/dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, 'Error validating the form')

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print('Successfull1')
        if form.is_valid():

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('/login')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


def authbase(request):
    return render(request, 'authbase.html')


def logout_req(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/register')


# def PasswordResetView(request):
#
#     return render(request, 'ResetPassword/password_reset_formm.html')