from django import urls
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('causes', views.causes, name="causes"),
    path('causes/<slug:slug>', views.cause_detail, name="cause_detail"),
    path('events', views.events, name="events"),
    path('events/<slug:slug>', views.event_detail, name="event_detail"),
    path('news', views.news, name="news"),
    path('news/<slug:slug>', views.story_detail, name="story_detail"),
    path('members', views.members, name="members"),
    path('members/<slug:slug>', views.member_detail, name="member_detail"),
    path('contact', views.contact, name="contact"),
]
