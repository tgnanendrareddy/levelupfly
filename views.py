from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.db import models

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def page2(request):
    return render(request,'page2.html')

def page1(request):
    return render(request,'page1.html')

def page3(request):
    return render(request,'page3.html')

def page4(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        
        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
        user.save()
        print('user created')
        return redirect('/')

    else:
        return render(request,'page4.html')

