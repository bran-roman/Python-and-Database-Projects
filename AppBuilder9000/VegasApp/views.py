from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import UserForm, ActivityForm, VegasNewsForm
import requests
import json
from . import views
from .models import Activities, User, VegasTemp, VegasNews
from newsapi import NewsApiClient
from django.contrib.auth import authenticate, login, logout
from django.urls import path
import datetime


def vegasapp_home(request):
    return render(request, 'VegasApp/vegasapp_home.html')


def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = ActivityForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('activity_page')
    else:
        return redirect('activity_page')


# Story #2: Create Model
def createUser(request):
    form = UserForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('../')
    else:
        print(form.errors)
        form = UserForm()
    content = {
        'form': form,
    }
    return render(request, 'VegasApp/createUser.html', content)


def createActivity(request):
    form = ActivityForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('../')
    else:
        print(form.errors)
        form = ActivityForm()
    content = {
        'form': form,
    }
    return render(request, 'VegasApp/createActivity.html', content)


# Story #3: Display all items from database
def activity_page(request):
    entry = Activities.objects.all()
    content = {'entry': entry}
    return render(request, 'VegasApp/activity_page.html', content)


# Story #4: Details Page
def activity_details(request, pk):
    entry = get_object_or_404(Activities, pk=pk)
    content = {'entry': entry}
    return render(request, 'VegasApp/activity_details.html', content)


# Story #5: Edit and Delete Functions

def activity_edit(request, pk):
    entry = get_object_or_404(Activities, pk=pk)
    form = ActivityForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../activity_page')
    content = {'form': form, 'entry': entry}
    return render(request, 'VegasApp/activity_edit.html', content)


def delete(request, pk):
    entry = get_object_or_404(Activities, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('activity_page')
    content = {'Activities': Activities}
    return render(request, 'VegasApp/confirmDelete.html', content)


# Story #6 + #7: Connect to API + Parse through JSON

# Note: Saving this API for potential use.
def vegasapp_api(request):
    query_params = {"q": 'vegas',
                    "sortBy": "top",
                    "apiKey": "568bc0fc6ea847bcb39944167ed66046"
                    }
    url = 'https://newsapi.org/v2/everything?q=Vegas&sortBy=popularity&apiKey=568bc0fc6ea847bcb39944167ed66046'

    response = requests.get(url, params=query_params)
    open_page = response.json()

    article = open_page["articles"]

    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        print(i + 1, results[i])
    content = results
    return render(request, 'VegasApp/vegasapp_saved_api.html', content)

def VegasNews():
    query_params = {"q": 'vegas',
                    "sortBy": "top",
                    "apiKey": "568bc0fc6ea847bcb39944167ed66046"
                    }

    url = 'https://newsapi.org/v2/everything?q=Vegas&sortBy=popularity&apiKey=568bc0fc6ea847bcb39944167ed66046'
    response = requests.get(url, params=query_params)
    open_bbc_page = response.json()

    article = open_bbc_page["articles"]

    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        print(i + 1, results[i])
#

#    form = VegasNewsForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        return redirect('../')
#    else:
#        print(form.errors)
#        form = VegasNewsForm
#    content = {'form': form}



# def vegasapp_api2(request):
#   url = "https://yahoo-weather5.p.rapidapi.com/weather"
#
#    querystring = {"location": "north las vegas", "format": "json", "u": "f"}
#
#    headers = {
#        "X-RapidAPI-Key": "fe17ebedd0msh8f1323cb434d97cp1efb2bjsnddc3ec7eace3",
#        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
#    }
#
#    response = requests.request("GET", url, headers=headers, params=querystring)
#
#    api_info = json.loads(response.text)
#    temp_int = api_info["current_observation"]["condition"]["temperature"]
#    current_temp = str(api_info["current_observation"]["condition"]["temperature"]) + ' \N{DEGREE SIGN} F'
#    content = {"current_temp": current_temp, "temp_int": temp_int}
#    return render(request, 'VegasApp/vegasapp_api.html', content)


# Story #8: Update Template Styling
def dining_page(request):
    return render(request, 'VegasApp/dining_page.html')


def attractions_page(request):
    return render(request, 'VegasApp/attractions_page.html')


def travel_page(request):
    return render(request, 'VegasApp/travel_page.html')


# Story #9: Save API

def vegasapp_save_api(request):
    if "state" in venues:
        venues = VegasNews.VegasNews.all()
        content = {"venues": venues}
    return render(request, 'VegasApp/vegasapp_save_api.html', venues)
