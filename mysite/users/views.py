from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import loginform
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def sign_in(request):
    if request.method == 'GET':
        form = loginform()
        return render(request, 'users/loginpage.html', {'form':form})
    elif request.method == 'POST':
        form = loginform(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi, {username.title()}, welcome back.')
                return redirect('posts')
        
        messages.error(request, f'Wrong username or password!')
        return render(request, 'users/login.html', {'form':form})