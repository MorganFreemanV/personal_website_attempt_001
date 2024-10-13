from django.shortcuts import render
from homepage.views import homepage_helloworld
from registration.forms import UserRegistration
from . import views
# Create your views here.

def signup_view(request):
    form = UserRegistration()
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('VALIDATION SUCCESS')
            return views.homepage_helloworld(request)
        else:
            print("ERROR FORM INVALID")
            

    return render(request, 'registration/signuppage.html', {'form':form})