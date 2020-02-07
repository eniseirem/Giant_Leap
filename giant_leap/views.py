from django.shortcuts import render
import requests
import json


key = "?api_key=V7RttlrR5x2ul8TvNpLCXo0CXNOvVS8VAw4HbkmT"

def homepage(request):
    response = requests.get('https://api.nasa.gov/planetary/apod'+key)
    apodata = response.json()

    return render(request, 'home.html', {'pics': apodata})
