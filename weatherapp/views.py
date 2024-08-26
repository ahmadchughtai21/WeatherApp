from django.shortcuts import render
import requests
import json

api ="YOUR_API_KEY"


# Create your views here.

def home(request):
    return render(request, 'home.html')

def report(request):
    global api
    
    data={
        'message': '',
        'city': '',
        'region': '',
        'country': '',
        'last_updated': '',
        'temp_c': '',
        'temp_f': '',
        'feelslike_c': '',
        'feelslike_f': '',
        'description': '',
        'is_day': '',
        'icon': '',
    }
    
    if request.method == 'POST':
        city = request.POST['city']
        URL = f"http://api.weatherapi.com/v1/current.json?key={api}&q={city}"
        
        result =requests.get(URL)

        if 'error' in result.json():
            data['message'] = result.json()['error']['message']
            return render(request, 'report.html', data)
        else:
            data['city'] = result.json()['location']['name']
            data['region'] = result.json()['location']['region']
            data['country'] = result.json()['location']['country']
            data['last_updated'] = result.json()['current']['last_updated']
            data['temp_c'] = result.json()['current']['temp_c']
            data['temp_f'] = result.json()['current']['temp_f']
            data['feelslike_c'] = result.json()['current']['feelslike_c']
            data['feelslike_f'] = result.json()['current']['feelslike_f']
            data['is_day'] = result.json()['current']['is_day']
            data['description'] = result.json()['current']['condition']['text']
            data['icon'] = result.json()['current']['condition']['icon']
            
            print(data['description'])
            return render(request, 'report.html', data)
    return render(request, 'report.html', data)
