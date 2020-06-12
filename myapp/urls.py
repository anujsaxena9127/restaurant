from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index,name='home'),
    path('home', views.home, name='home'),
     path('aboutUs', views.aboutUs,name='aboutUs'),
    path('menu', views.menu,name='menu'),
    path('reservations', views.reservations,name='reservations'),
    path('contact', views.contact,name='contact'),
    path('gallery', views.gallery,name='gallery')

]
