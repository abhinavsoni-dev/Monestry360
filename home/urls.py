from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.home, name='home'),
    path('archive/', include('archive.urls')),
    path('calendar/', include('calendar.urls')),
    path('virtualtour/', include('virtualtour.urls')),
    path('monasteries/', include('monasteries.urls')),
    path('search/', include('search.urls')),
]
