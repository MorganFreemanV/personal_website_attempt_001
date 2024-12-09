from django.urls import re_path, path 
from register import views
from homepage.views import homepage_helloworld


urlpatterns = [
    re_path(r'^$', views.register_page, name='register_page'),
    re_path('', homepage_helloworld, name='homepage')
    
]
app_name = 'register'