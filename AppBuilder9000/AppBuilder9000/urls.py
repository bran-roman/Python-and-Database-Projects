"""AppBuilder9000 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings    #FOR PILLOW LIBRARY
#from django.conf.urls.static import static     #FOR PILLOW LIBRARY
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('Journal/', include('Journal.urls')),
    path('contactBook/', include('contactBook.urls')),
    path('Bicycles/', include('Bicycles.urls')),
    path('PetsApp/', include('PetsApp.urls')),
    path('NativePlants/', include('NativePlants.urls')),
    path('Traveling/', include('Traveling.urls')),
    path('DailyBugle/', include('DailyBugle.urls')),
    path('Meal_Tracker/', include('Meal_Tracker.urls')),
    path('BowlingRocks/', include('BowlingRocks.urls')),
    path('YoMamasRecipes/', include('YoMamasRecipes.urls')),
    path('Basketball/', include('Basketball.urls')),
    path('SecretSanta/', include('SecretSanta.urls')),
    path('InternetCulture/', include('InternetCulture.urls')),
    path('PortlandDining/', include('PortlandDining.urls')),
    path('HockeyTracker/', include('HockeyTracker.urls')),
    path('BookChallenge/', include('BookChallenge.urls')),
    path('WhiskeyLog/', include('WhiskeyLog.urls')),
    path('VegasApp/', include('VegasApp.urls')),
    path('ShoeLibrary/', include('ShoeLibrary.urls')),
    path('MoviePicker/', include('MoviePicker.urls')),
    path('CostaRicaApp/', include('CostaRicaApp.urls')),
    path('CarMaintenanceTracker/', include('CarMaintenanceTracker.urls')),
]

# urlpatterns +=staticfiles_urlpatterns()

# if settings.DEBUG:  # FOR PILLOW LIBRARY
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
