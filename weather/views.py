from django.shortcuts import render, redirect
import requests
from requests.sessions import ContentDecodingError, Request
from .models import City
from django.http import HttpResponse
from .models import City
from .forms import CityForm

def errorPage(request):
    return render(request, 'weather/error_page.html')   

def homePage(request):
    cities=City.objects.all()
    form=CityForm()

    if request.method=='POST':
        city_name=request.POST['city']
        form=CityForm(request.POST)
        if form.is_valid():
            form.save()
         
        url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=2eaa371d6a51269823ba337bcc52873b&units=metric&lang=en"
        r=requests.get(url.format(city_name)).json()
        
        weather={  
                'city': city_name,
                'temperature' : r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
                                        
            }            
    else:
        weather={}

    context={'weather':weather, "form":form, "cities":cities}                
    return render(request, 'weather/index.html',context)
    

def dashboardPage(request):
    form=CityForm()
    city=City.objects.all()
    if request.method=='POST':
        form=CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        context={'form':form}
        return render(request, 'weather/add_city.html',context)
        
def editPage(request):
    pass        