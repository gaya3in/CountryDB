from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Country,TimeZones, Translations,State,City
import json
from .utils import connect_db

# Create your views here.
""" 
 Render Home Page. Get data from Country table and display the Countries 
"""
def home(request):

    if request.method == "GET":
        try:
            countries = Country.objects.all()
            context = {"countries": countries}
            return render(request, "home.html", context)
        except Exception as e:
            print(e)

""" 
 Get data from State table and display all the states or the selected country 
"""
def get_country_data(request):
    if request.method == "POST":
        try:
            data = request.POST
            print(data)
            country_id = data['countryid']
            action = data['action']
            print("countryId:", country_id)
            print("Action:", action)

            if action == "states":
                results = connect_db(country_id, action)
                return JsonResponse(results, safe=False)
        except Exception as e:
            print(e)

""" 
 Get data from City table and display all the cities or the selected state 
"""
def get_state_data(request):
    if request.method == "POST":
        try:
            data = request.POST
            print(data)
            state_id = data['stateid']
            action = data['action']
            print("stateId:", state_id)
            print("Action:", action)

            if action == "cities":
                results = connect_db(state_id, action)
                return JsonResponse(results, safe=False)
        except Exception as e:
            print(e)

""" 
 Get more details for the selected country
"""
def get_country_details(request):
    if request.method == "POST":
        try:
            data = request.POST
            print(data)
            country_id = data['countryid']
            action = data['action']
            print("countryId:", country_id)
            print("Action:", action)

            if action == "country_details":
                results = connect_db(country_id, action)
                results = json.dumps(results, indent=2)
                print(type(results))
                print(results)
                return JsonResponse(results, safe=False)
        except Exception as e:
            print(e)

""" 
 Get more details for the selected state
"""
def get_state_details(request):
    if request.method == "POST":
        try:
            data = request.POST
            print(data)
            state_id = data['stateid']
            action = data['action']
            print("stateId:", state_id)
            print("Action:", action)

            if action == "state_details":
                results = connect_db(state_id, action)
                results = json.dumps(results, indent=2)
                return JsonResponse(results, safe=False)
        except Exception as e:
            print(e)

""" 
 Get more details for the selected city
"""
def get_city_details(request):
    if request.method == "POST":
        try:
            data = request.POST
            print(data)
            city_id = data['cityid']
            action = data['action']
            print("cityId:", city_id)
            print("Action:", action)

            if action == "city_details":
                results = connect_db(city_id, action)
                results = json.dumps(results, indent=2)
                return JsonResponse(results, safe=False)
        except Exception as e:
            print(e)