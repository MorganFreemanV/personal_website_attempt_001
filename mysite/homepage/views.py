from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import *

# Create your views here.

def homepage_helloworld(request):
    webpage_list = AccessRecord.objects.order_by('date')
    webpage_list = reversed(webpage_list)
    date_dict = {'access_records':webpage_list}
    # return HttpResponse('<h1>Hello world!</h1>')
    mydict = {'insert_me':'Hello I am from views.py'}
    #return render(request, 'homepage/homepage.html', context=mydict)
    #return render(request, 'homepage/homepage.html', context=date_dict)
    return render(request, 'homepage/homepage.html', context=date_dict)

def users_page(request):
    names_list = Users.objects.order_by('first_name','last_name', 'emailadd')
    name_dict = {'user_names':names_list}
    return render(request, 'homepage/users.html', context=name_dict)
