"""CountryDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home, get_country_data, get_state_data, \
                   get_country_details,get_state_details, get_city_details

urlpatterns = [
    path('', home, name="home"),
    path('getcountrydata/', get_country_data, name="get_country_data"),
    path('getstatedata/', get_state_data, name="get_state_data"),
    path('getcountrydetails/', get_country_details, name="get_country_details"),
    path('getstatedetails/', get_state_details, name="get_state_details"),
    path('getcitydetails/', get_city_details, name="get_city_details"),

]
