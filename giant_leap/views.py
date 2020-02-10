from django.shortcuts import render
import requests
import json


key = "?api_key=V7RttlrR5x2ul8TvNpLCXo0CXNOvVS8VAw4HbkmT"

def homepage(request):
    response = requests.get('https://api.nasa.gov/planetary/apod'+key)
    data = response.json()
    imgList = []
    imgList.append(data)


    if 'search' in request.GET:
        search_term = request.GET['search']
        response = requests.get('https://images-api.nasa.gov/search?q='+search_term)
        #apodata = response.json()['collection']['items'][0]['links'][0]['href']
        apodata = response.json()['collection']['items']
        imgList.clear()
        for x in apodata:
            placeImg = {'explanation': '', 'url': ''}
            #imgList.append({'description':'desc here', 'href':x['links'][0]['href']})

            try:
                placeImg['explanation'] = x['data'][0]['description']
            except KeyError:
                placeImg['explanation'] = x['data'][0]['title']

            #placeImg['href'] = x['links'][0]['href']
            try:
                placeImg['url'] = x['links'][0]['href']
            except KeyError:
                continue
            imgList.append(placeImg)

        print('IMG LIST BITTI')
        print(imgList)

        #apodata_dict = json.loads(apodata)
        #
        # for apoddata in apodata:
        #     for link in apoddata['links']:
        #         if link['rel'] == 'preview':
        #          url=link['href']
        #     for info in apoddata['data']:
        #         title=info['title']
        #         description=info['description']

        # data['url']=[x[0]['links'][0]['href'] for x in apodata if x]
        # data['title']=[x['data']['title'] for x in apodata]
       # apodata=ptojson(apodata)
   #     for x in apodata:
  #          for y in x.links:
 #               if y['rel'] == 'preview':
#                    url=y['href']

    return render(request, 'home.html', {'pics': imgList})


def ptojson(json1):
    pyth2json = json.dumps(json1)
    return pyth2json
