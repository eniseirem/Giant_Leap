from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from django.contrib.auth import login, authenticate, logout
from giant_leap.forms import SignUpForm
from django.contrib.auth.decorators import login_required


key = "?api_key=V7RttlrR5x2ul8TvNpLCXo0CXNOvVS8VAw4HbkmT"

@login_required
def homepage(request):
    response = requests.get('https://api.nasa.gov/planetary/apod'+key)
    data = response.json()
    imgList = []
    imgList.append(data)


    if 'search' in request.GET:
        search_term = request.GET['search']
        response = requests.get('https://images-api.nasa.gov/search?q='+search_term)
        apodata = response.json()['collection']['items']
        imgList.clear()
        for x in apodata:
            placeImg = {'explanation': '', 'url': ''}

            try:
                placeImg['explanation'] = x['data'][0]['description']
            except KeyError:
                placeImg['explanation'] = x['data'][0]['title']

            try:
                placeImg['url'] = x['links'][0]['href']
            except KeyError:
                continue
            imgList.append(placeImg)

        print('IMG LIST BITTI')
        print(imgList)

    return render(request, 'home.html', {'pics': imgList})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
        if request.user.is_authenticated:
            return homepage(request)
        else:
            return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        if request.user.is_authenticated:
            return homepage(request)
        else:
            return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')