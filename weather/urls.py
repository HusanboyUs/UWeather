from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='mainPage'),
    path('about/', views.aboutPage, name='aboutPage'),
    #path('error/', views.errorPage, name='error_page')
]
