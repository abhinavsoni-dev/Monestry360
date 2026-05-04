from django.urls import path
from . import views

app_name = 'monasteries'
urlpatterns = [
    path("maps/", views.maps, name='maps'),
    path("rumtek/", views.rumtek, name='rumtek'),
    path("tsechey/", views.tsechey, name='tsechey'),
    path("tsukla/", views.tsukla, name='tsukla'),
    path("pemayangtse/", views.pemayangtse, name='pemayangtse'),
]
