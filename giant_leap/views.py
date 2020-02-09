from django.shortcuts import render
import requests
import json


key = "?api_key=V7RttlrR5x2ul8TvNpLCXo0CXNOvVS8VAw4HbkmT"

def homepage(request):
    response = requests.get('https://api.nasa.gov/planetary/apod'+key)
    apodata = response.json()


    if 'search' in request.GET:
        search_term = request.GET['search']
        response = requests.get('https://images-api.nasa.gov/search?q='+search_term)
        search_data = response.json()
        #for data in search_data.collection.data:


        #print(apodata)


    return render(request, 'home.html', {'pics': apodata})

