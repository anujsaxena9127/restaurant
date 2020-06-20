from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('', views.index,name='home'),
    path('home', views.home, name='home'),
    
    path('menu', views.menu,name='menu'),
    path('reservations', views.reservations,name='reservations'),
    path('contact', views.contact,name='contact'),
    path('gallery', views.gallery,name='gallery'),
    path('signup', views.handleSignup, name='handlesSignup'),
    path('login', views.handlelogin, name='handleslogin'),
    path('logout', views.handlelogout, name='handleslogout'),
    path('accounts/', include('allauth.urls')),

]
