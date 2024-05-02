# from django.http import HttpResponse
from django.shortcuts import render
from car.models import UserDetail

# Create your views here.

def home(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        login_instance = UserDetail.objects.create(firstname=firstname, lastname=lastname, phone=phone, email=email, password=password)

        login_instance.save()

        return render(request,'index.html')
    else:
        return render(request,'register.html')
    

def login(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')