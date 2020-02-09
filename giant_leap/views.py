from django.shortcuts import render, redirect
import requests
from django.contrib.auth import login, authenticate
from giant_leap.forms import SignUpForm

key = "?api_key=V7RttlrR5x2ul8TvNpLCXo0CXNOvVS8VAw4HbkmT"

def homepage(request):
    response = requests.get('https://api.nasa.gov/planetary/apod'+key)
    apodata = response.json()

    return render(request, 'home.html', {'pics': apodata})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
