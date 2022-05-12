from django.core.cache import cache
import requests
from city.models import City

def getCityCurrent(id = 1):
    cityTitle = City.objects.get(id = id)
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={cityTitle.latitude}&lon={cityTitle.longitude}&exclude=minutely%2Chourly%2Cdaily%2Calerts&appid=722059280fa10626b86d900c6e39a326&lang=vi&units=metric"
    cityJSON = requests.get(url).json()

    city = {
        "name": cityTitle.name,
        "temp": round(cityJSON["current"]["temp"]),
        "icon": f"http://openweathermap.org/img/wn/{cityJSON['current']['weather'][0]['icon']}@2x.png",
        "description": cityJSON["current"]['weather'][0]['description'].capitalize(),
        "pressure": cityJSON["current"]["pressure"],
        "humidity": cityJSON["current"]["humidity"],
        "dew_point": round(cityJSON["current"]["dew_point"]),
        "uvi": cityJSON["current"]["uvi"],
        "clouds": cityJSON["current"]["clouds"],
        "wind_speed": cityJSON["current"]["wind_speed"],
        "feels_like": round(cityJSON["current"]["feels_like"]),
        "url": url,
    }

    return city

def getAllCityName():
    allCity = City.objects.all()
    
    allCityName = list()
    for city in allCity:
        allCityName.append({"id": str(city.id), "name": city.name})

    return allCityName

def getDailyCity(id=58):

    # daily = cache.get('daily'+id)
    # if daily is not None:
    #     return daily

    cityTitle = City.objects.get(id = id)
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={cityTitle.latitude}&lon={cityTitle.longitude}&exclude=current,minutely,hourly,alerts&appid=722059280fa10626b86d900c6e39a326&lang=vi&units=metric"
    cityJSON = requests.get(url).json()

    daily = list()

    for day in cityJSON["daily"]:
        cityDaily = {
            "temp": day["temp"]["day"],
            "rain": day.get("rain", 0),
            "uvi": day["uvi"],
            "clouds": day["clouds"]
        }

        daily.append(cityDaily)
        
    cache.set('daily'+id, daily, 60*60*24)

    return daily
