# views.py

from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import City
from .forms import CityForm


# home page
def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=1d5b8a70f7a80f27141062e9f309bd73'

    if request.method == 'POST':
        if 'city_id' in request.POST:
            city_id = request.POST['city_id']
            if city_id == '0':
                # Clear city list
                City.objects.all().delete()
            else:
                # Delete selected city
                city = get_object_or_404(City, pk=city_id)
                city.delete()
        else:
            form = CityForm(request.POST)
            if form.is_valid():
                form.save()

    form = CityForm()
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        if 'main' in city_weather:
            city_weather = {
                'id': city.id,
                'city': city.name,
                'temperature': round((city_weather['main']['temp'] - 32) * 5/9),
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon'],
            }
            weather_data.append(city_weather)
        else:
            city.delete()

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'home.html', context)
