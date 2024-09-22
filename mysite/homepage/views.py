from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage_helloworld(request):
    # return HttpResponse('<h1>Hello world!</h1>')
    mydict = {'insert_me':'Hello I am from views.py'}
    return render(request, 'homepage/homepage.html', context=mydict)