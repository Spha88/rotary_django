from django import urls
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('causes', views.causes, name="causes"),
    path('events', views.events, name="events"),
    path('news', views.news, name="news"),
]
