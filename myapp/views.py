from datetime import datetime

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
# from myapp.models import Contact
from .models import booking, table


def index(request):
    return render(request, 'index.html')


def home(request):


    return render(request, 'index.html')


def aboutUs(request):
    return render(request, 'aboutUs.html')


def menu(request):
    return render(request, 'menu.html')


def reservations(request):



    if request.method == "POST":
        name = request.POST.get('name')
        date = request.POST.get('date')
        email= request.POST.get('email')
        time = request.POST.get('time')
        phone = request.POST.get('phone')
        people = request.POST.get('people')
        message = request.POST.get('message')


        reservations = table(name=name, date=date,email=email,time=time ,phone=phone, people=people, message=message)

        reservations.save()

    return render(request, 'reservations.html')


def contact(request):
    if not request.user.is_authenticated:
        messages.error(request,'First Login In ')
        return render(request, 'index.html')


    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = booking(name=name, email=email, subject=subject, message=message)

        contact.save()

    return render(request, 'contact.html')


def gallery(request):

    return render(request, 'gallery.html')


def handleSignup(request):
    if request.method == 'POST':
        # get the post parameters#
        username = request.POST['username']
        fname = request.POST['fname1']
        lname = request.POST['lname1']
        email = request.POST['email1']
        password1 = request.POST['password2']
        password2 = request.POST['password4']

        # checks for error in filling form
        #validating signupup form
        if len(username)>10:
            messages.error(request,"username must be be under 10 character")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "username must be contain letters and numbers")
            return redirect('home')



        if password1!=password2:
            messages.error(request, "password doesnt match")
            return redirect('home')

        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account is successfully created")
        return redirect('home')




    return HttpResponse('404 not found')

def handlelogin(request):
    if request.method == 'POST':
        # get the post parameters#
        username = request.POST['username']
        password= request.POST['password6']

        user =authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully loggged in")
            return redirect('home')
        else:
            messages.success(request,'Invalid creditianials')

    return HttpResponse('404 not found')

def handlelogout(request):
    logout(request)
    messages.success(request,"Suucessfully logged out")
    return redirect('home')
    return HttpResponse('handlelogout')