from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def vehicles(request):
    return render(request,'vehicles.html')

def vehicle_data(request):
    return render(request,'vehicle_details.html')

def contact(request):
    return render(request,'contact.html')

def news(request):
    return render(request,'news_slidbar.html')

def blog(request):
    return render(request,'includes/blog/blog_data.html')