from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    vehicle_data = Vehicles.objects.filter().order_by('created_at')[:4]
    latest_vehicle = Vehicles.objects.filter().order_by('-created_at')[:3]
    footer_show_vehicle = Vehicles.objects.filter().order_by('-created_at')[:5]
    context={
        'vehicle_data':vehicle_data,
        'latest_vehicle':latest_vehicle,
        'footer_data':footer_show_vehicle
    }
    return render(request,'index.html',context)

def about(request):
    vehicle_data = Vehicles.objects.all()
    latest_vehicle = Vehicles.objects.filter().order_by('-created_at')[:3]
    footer_show_vehicle = Vehicles.objects.filter().order_by('-created_at')[:5]
    context={
        'vehicle_data':vehicle_data,
        'latest_vehicle':latest_vehicle,
        'footer_data':footer_show_vehicle
    }
    return render(request,'about.html',context)

def vehicles(request):
    vehicle_data = Vehicles.objects.all().order_by('created_at')
    get_data=Paginator(vehicle_data,6)

    page_number=request.GET.get('page')
    page_data=get_data.get_page(page_number)

    latest_vehicle = Vehicles.objects.filter().order_by('-created_at')[:3]
    footer_show_vehicle = Vehicles.objects.filter().order_by('-created_at')[:5]
    context={
        'vehicle_data':page_data,
        'page_data': page_data,
        'latest_vehicle':latest_vehicle,
        'footer_data':footer_show_vehicle
    }
    return render(request,'vehicles.html',context)

def vehicle_data(request,id):
    
    try:
        vehicle_data = Vehicles.objects.get(vehicle_id=id)
    except Vehicles.DoesNotExist:
        return redirect('Home_Page')
    
    latest_vehicle = Vehicles.objects.filter().order_by('-created_at')[:3]
    footer_show_vehicle = Vehicles.objects.filter().order_by('-created_at')[:5]
    context={
        'vehicle_data':vehicle_data,
        'latest_vehicle':latest_vehicle,
        'footer_data':footer_show_vehicle,
    }
    return render(request,'vehicle_details.html',context)

def contact(request):
    vehicle_data = Vehicles.objects.all()
    latest_vehicle = Vehicles.objects.filter().order_by('-created_at')[:3]
    footer_show_vehicle = Vehicles.objects.filter().order_by('-created_at')[:5]
    customer_enquiry = None

    # Enduiry data geting
    if request.method == "POST":
        try:
            Name = request.POST.get("Name")
            Email = request.POST.get("Email")
            Number = request.POST.get("Phone")
            Message = request.POST.get("Message")

            if not Name or not Email or not Number or not Message:
                messages.error(request, "All fields are required. Please fill out the form completely.")
                return redirect("Contact_Us")
            else:
                customer_enquiry = Contact.objects.create(
                    name=Name,email=Email,phone=Number,message=Message)
                customer_enquiry.save()
                messages.success(request, "Your enquiry has been submitted successfully!")
                return redirect("Contact_Us")
        
        except Exception as e:
            messages.error(request, "There was a problem submitting your enquiry. Please try again.")


    context={
        'vehicle_data':vehicle_data,
        'enquiry':customer_enquiry,
        'latest_vehicle':latest_vehicle,
        'footer_data':footer_show_vehicle,
    }
    return render(request,'contact.html',context)

def news(request):
    vehicle_data = Vehicles.objects.all()
    latest_vehicle = Vehicles.objects.filter().order_by('-created_at')[:3]
    footer_show_vehicle = Vehicles.objects.filter().order_by('-created_at')[:5]
    context={
        'vehicle_data':vehicle_data,
        'latest_vehicle':latest_vehicle,
        'footer_data':footer_show_vehicle,
    }
    return render(request,'news_slidbar.html',context)

def blog(request):
    vehicle_data = Vehicles.objects.all()
    latest_vehicle = Vehicles.objects.filter().order_by('-created_at')[:3]
    footer_show_vehicle = Vehicles.objects.filter().order_by('-created_at')[:5]
    context={
        'vehicle_data':vehicle_data,
        'latest_vehicle':latest_vehicle,
        'footer_data':footer_show_vehicle,
    }
    return render(request,'includes/blog/blog_data.html',context)