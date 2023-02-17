from django.shortcuts import render, redirect
import requests
from requests import get, Session
from django.http import HttpResponse
from django.contrib import messages
from urllib import response
from googleplaces import GooglePlaces, types, lang
from .forms import InputForm
from django.contrib import messages
# Create your views here.

def home(request):

    user_ip = get_ip_address(request)
    

    data = {}
    
    if request.method == 'POST':

        ipaddress = request.POST['ipaddress']

        endpoint = 'http://api.ipstack.com/'

        headers = endpoint + ipaddress + '?access_key=62aa7717849fac797f69371812963091'

        get_response = requests.get(headers)

        data = get_response.json()

        if data['continent_code'] == 'AF':
            messages.info(request, 'You are welcome')
        else:
            messages.info(request, 'Hey! You do not have access to this page')

    return render(request, 'index.html', {'data': data})




def get_ip_address(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def github_api(request):

    endpoint = 'https://coronavirus.m.pipedream.net/'
    
    response = requests.get(endpoint)

    data = response.json()

    rawdata = data['rawData']

    deathrate = [i['Deaths'] for i in rawdata]
    

    res = [eval(i) for i in deathrate]
    maximum_death = max(res)
    for i in rawdata:
        if i['Deaths'] == str(maximum_death):
            cases = i

            print(cases)
            
            Latitude = cases['Lat']
            
            Longitude = cases['Long_']
            


        # API_KEY = 'AIzaSyDflVXxDLQdJyBIlQoTOThMX3YToQouoHU'

        
        # google_places = GooglePlaces(API_KEY)


        # query_result = google_places.nearby_search(
                
        #         lat_lng ={'lat': 2.8994, 'lng': -3.8889},
        #         radius = 5000,
                
        #         types =[types.TYPE_HOSPITAL])


        # if query_result.has_attributions:
        #     print (query_result.html_attributions)



        # for place in query_result.places:
        #     print(place)
        #     print (place.name)
        #     print("Latitude", place.geo_location['lat'])
        #     print("Longitude", place.geo_location['lng'])
        #     print()


    
    

   
            
    


        
    return render(request, 'githubprojects.html', {'case_studys':cases})

def paypal(request):
    return render(request, 'checkout.html')


def transfer(request):
    context ={}
    context['form']= InputForm()

    return render(request, 'notification.html', context)








    






