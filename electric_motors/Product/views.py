from django.shortcuts import render
from . models import *

# Create your views here.

def home(request):
    vehicle_data=Vehicles.objects.all()
    context={
        'vehicle_data':vehicle_data
    }
    return render(request,'index.html',context)

def about(request):
    vehicle_data=Vehicles.objects.all()
    context={
        'vehicle_data':vehicle_data
    }
    return render(request,'about.html',context)

def vehicles(request):
    vehicle_data=Vehicles.objects.all()
    context={
        'vehicle_data':vehicle_data
    }
    return render(request,'vehicles.html',context)

def vehicle_data(request):
    vehicle_data=Vehicles.objects.all()
    context={
        'vehicle_data':vehicle_data
    }
    return render(request,'vehicle_details.html',context)

def contact(request):
    vehicle_data=Vehicles.objects.all()
    context={
        'vehicle_data':vehicle_data
    }
    return render(request,'contact.html',context)

def news(request):
    vehicle_data=Vehicles.objects.all()
    context={
        'vehicle_data':vehicle_data
    }
    return render(request,'news_slidbar.html',context)

def blog(request):
    vehicle_data=Vehicles.objects.all()
    context={
        'vehicle_data':vehicle_data
    }
    return render(request,'includes/blog/blog_data.html',context)