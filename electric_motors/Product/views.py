from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

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