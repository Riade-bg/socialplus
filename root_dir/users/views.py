from django.shortcuts import render, redirect
from .forms import UserRegestraionForm, UserUpdateForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegestraionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account Has Been Created Successfully.')
            return redirect('/')
    else:
        form = UserRegestraionForm()
    contex = {
        'form':form
    }
    return render(request, 'users/register.html', contex)

@login_required
def setting(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:home')
    else:
        form = UserUpdateForm(instance = request.user)
    contex = {
        'form':form
    }
    return render(request, 'social/settings.html', contex)



