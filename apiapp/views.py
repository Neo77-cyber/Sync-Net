from django.shortcuts import render
import requests
from requests import get
from django.http import HttpResponse
from django.contrib import messages
from urllib import response
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def restricted_ipadress_access(request):

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

    return render(request, 'restrictedip.html', {'data': data})

# Use this in production
def get_ip_address(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def max_covid19_death_rate(request):

    endpoint = 'https://coronavirus.m.pipedream.net/'
    
    response = requests.get(endpoint)

    data = response.json()

    rawdata = data['rawData']

    deathrate = [i['Deaths'] for i in rawdata]
    

    res = [eval(i) for i in deathrate]
    
    maximum_death = max(res)
    
    cases = []
    for i in rawdata:
        if i['Deaths'] == str(maximum_death):
            cases.append(i)
    return render(request, 'maxcoviddeathrate.html', {'cases':cases})

def paypalcheckout(request):
    return render(request, 'paypalcheckout.html')

def sociallogin(request):
    return render(request, 'sociallogin.html')

def otp_login(request):

    return render(request, 'otplogin.html')
    







    






