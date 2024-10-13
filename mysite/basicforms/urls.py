from django.urls import re_path, path
from basicforms import views

urlpatterns = [
    re_path(r'^basicforms/', views.form_name_view, name='forms_page'),
]