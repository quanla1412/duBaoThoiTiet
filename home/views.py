import logging
from django.shortcuts import render

from home import chart
from . import methods

# Create your views here.
def index(request):

    id = request.GET.get('id') if request.GET.get('id') is not None else "58"
    
    city = methods.getCityCurrent(id)
    allCityName = methods.getAllCityName()

    allChart = chart.getAllChart(id)
    
    Data = {
        "City": city,
        "allCityName": allCityName,
        "idCurrent": id,
        "charts": allChart, 
    }

    return render(request, "pages/home.html", Data)
    