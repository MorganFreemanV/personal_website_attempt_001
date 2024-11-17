from django.shortcuts import render


# Create your views here.

def register_page(request):
    return render(request, 'register/registration.html')
    """ webpage_list = AccessRecord.objects.order_by('date')
    webpage_list = reversed(webpage_list)
    date_dict = {'access_records':webpage_list}
    # return HttpResponse('<h1>Hello world!</h1>')
    mydict = {'insert_me':'Hello I am from views.py'}
    #return render(request, 'homepage/homepage.html', context=mydict)
    #return render(request, 'homepage/homepage.html', context=date_dict)
    return render(request, 'homepage/homepage.html', context=date_dict) """