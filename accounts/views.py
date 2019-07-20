from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm
)
from .forms import UserRegistrationForm

def home_view(request):
    return render(request, 'accounts/base.html')

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('tracker:home')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }

    return render(request, 'accounts/signin.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Your are now able to log in')
            return redirect('accounts:signin')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form':form})

def logout_view(request):
        logout(request)
        return redirect('accounts:home_view')
