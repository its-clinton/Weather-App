from django.shortcuts import render, redirect
import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


# home page
def weather(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=1d5b8a70f7a80f27141062e9f309bd73'

    cities = City.objects.all()
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()
    
    weather_data = []

    for city in cities:
            
            city_weather = requests.get(url.format(city)).json()
            
            if 'main' in city_weather:
                city_weather = {
                    'city' : city.name,
                    'temperature' : round((city_weather['main']['temp'] - 32) * 5/9),
                    'description' : city_weather['weather'][0]['description'],
                    'icon' : city_weather['weather'][0]['icon'],
                }
                weather_data.append(city_weather)
            else:
                city.delete()
                break
                
    context = {'weather_data' : weather_data, 'form' : form}
    
    return render(request, 'home.html', context)

# delete city
def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()

    return redirect('home')



