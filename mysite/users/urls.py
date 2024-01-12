from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.sign_in, name='login'), 
    #views.IndexView.as_view(), name='helloworld'),
    #path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    #path("<int:question_id>/vote/", views.vote, name="vote"),
]

'''
https://www.pythontutorial.net/django-tutorial/django-login/
'''