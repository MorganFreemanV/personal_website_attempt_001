from django.urls import re_path, path
from registration import views

urlpatterns = [
    re_path(r'^$', views.signup_view, name='signup_view'),
]

app_name = 'registration'