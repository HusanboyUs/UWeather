from django.shortcuts import render, redirect
import requests
from .models import City
from django.http import HttpResponse



def errorPage(request):
    return render(request, 'weather/error_page.html')   

def homePage(request):
    
    try:
        if request.method=='POST':
            city_name=request.POST['city_name']
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
        
        return render(request, 'weather/index.html',weather )
    except:
        return errorPage(request)


def aboutPage(request):
     return render(request, 'weather/about.html')
   
#cheking up on friends is cool