from django.urls import re_path, path 
from homepage import views
from register.views import register_page

urlpatterns = [
    
    re_path(r'^$', views.homepage_helloworld, name='homepage_helloworld'),
    path('users/', views.users_page, name='users_page'),
    path('register/', register_page, name='register_page'),
]