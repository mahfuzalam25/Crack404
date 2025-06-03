from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('websites', views.websites, name='websites'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('team', views.team, name='team'),
    path('career', views.career, name='career'),
    path('contact', views.contact, name='contact'),
]