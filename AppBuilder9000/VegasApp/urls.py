from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vegasapp_home, name='vegasapp_home'),
    path('dining/', views.dining_page, name="dining_page"),
    path('attractions/', views.attractions_page, name="attractions_page"),
    path('travel/', views.travel_page, name="travel_page"),
    path('createUser/', views.createUser, name="createUser"),
    path('createActivity/', views.createActivity, name="createActivity"),
    path('activity_page/', views.activity_page, name="activity_page"),
    path('<int:pk>/details/', views.activity_details, name="activity_details"),
    path('<int:pk>/edit/', views.activity_edit, name="activity_edit"),
    path('<int:pk>/delete/', views.delete, name="confirmDelete"),
    path('confirmDelete/', views.confirmed, name="confirmed"),
    path('api/', views.vegasapp_api, name="vegasapp_api"),
    path('<int:m>/save_api/', views.vegasapp_save_api, name='vegasapp_save_api'),
    path('vegasNews/', views.VegasNews, name="VegasNews"),
]
