from django.shortcuts import render

from user.forms import  UserLoginForm
from django.http import JsonResponse
import requests
# Create your views here.

# --This area for static pages of the website or Front End Pages ------------------>

def Home_Page(request):
    return render(request, 'frontend/home.html')

def Login_page(request):
    return render(request, 'frontend/login_page.html')

def Registration_page(request):
    return render(request, 'frontend/registration_page.html')

def Logout_page(request):
    return render(request, 'frontend/login_page.html')


def get_location_data(pincode):
    try:
        
        response = requests.get(f'http://api.postalpincode.in/pincode/{pincode}')
        data = response.json()
    
        if response.status_code == 200:
            city = data[0]['PostOffice'][0]['District']
            state = data[0]['PostOffice'][0]['State']
            country = data[0]['PostOffice'][0]['Country']
             
            print(city,state, country)
            return city,state, country
        else:
            return None,None, None
    except Exception as e:
        print(f"Error fetching location data: {e}")
        return None,None, None

def location_view(request):
    pincode = request.GET.get('pincode')
   
    print(pincode)
    if pincode:
        city,state, country = get_location_data(pincode)
        if city and state and country:
            return JsonResponse({
                "city": city, 
                "state": state,
                "country": country})
        else:
            return JsonResponse({"error": "Location not found"})
    return JsonResponse({"error": "No pincode provided"})        


