from django.urls import re_path 
from homepage import views

urlpatterns = [
    
    re_path(r'^$', views.homepage_helloworld, name='homepage_helloworld'),
]