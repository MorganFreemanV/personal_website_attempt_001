from django.urls import re_path, path 
from homepage import views

urlpatterns = [
    
    re_path(r'^$', views.homepage_helloworld, name='homepage_helloworld'),
    path('users/', views.users_page, name='users_page'),
]