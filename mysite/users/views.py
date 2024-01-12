from django.shortcuts import render
from django.http import HttpResponse
from .forms import loginform

# Create your views here.

def sign_in(request):
    if request.method == 'GET':
        form = loginform()
        return render(request, 'users/loginpage.html', {'form':form})