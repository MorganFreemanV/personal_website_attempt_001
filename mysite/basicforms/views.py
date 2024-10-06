from django.shortcuts import render
from . import forms
from django.contrib.auth.models import User
# Create your views here.

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('VALIDATION SUCCESS')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])
            

    return render(request, 'basicforms/basicform.html', {'form':form})

def signup_view(request):
    form = forms.LoginData()
    if request.method == 'POST':
        form = forms.LoginData(request.POST)
        email = request.POST['email_add']
        if form.is_valid():
            form.save()
            print('VALIDATION SUCCESS')
            

    return render(request, 'basicforms/signuppage.html', {'form':form})

