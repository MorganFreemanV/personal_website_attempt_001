from django.urls import re_path, path 
from register import views

urlpatterns = [
    re_path(r'^$', views.register_page, name='register_page'),
    
]