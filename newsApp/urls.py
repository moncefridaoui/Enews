from django.urls import path

from . import views

app_name='newsApp'

urlpatterns=[
    path('', views.News, name='News'),  
]