from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='mainPage'),
    path('dashboardPage/', views.dashboardPage, name='dashboardPage')
    
]
