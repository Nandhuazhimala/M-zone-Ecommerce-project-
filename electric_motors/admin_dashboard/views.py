from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from . models import Profile
from django.core.paginator import Paginator
from Product. models import *

# Create your views here.

# User Login section
def admin_login(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')

        user= auth.authenticate(username=Username,password=Password)
        if user is not None:
            if user.is_superuser:
                auth.login(request, user)
                messages.info(request, " Admin Logged Successfully!!")
                return redirect('Admin_Dashboard')
            else:
                auth.login(request, user)
                messages.info(
                    request, f"{user.username} is Logged Successfully!!")
                return redirect('Admin_Dashboard')
        else:
            messages.info(request, 'Username or Password is Incorrect.')
            return redirect('Admin_Login')
            
    return render(request,'dashboard/authentication/login.html')

# User Register Section
def admin_register(request):
    if request.method == 'POST':
        try:
            Username = request.POST.get('full_name')
            Email = request.POST.get('email')
            Password = request.POST.get('password')
            Confirm_password = request.POST.get('confirm_password')
            Profile_img = request.FILES.get('profile_image')

            if Password != Confirm_password:
                messages.error(request, "Oops! The Password and Confirm Password fields don’t match. Please re-enter them.")
                return redirect('Admin_Register')

            if User.objects.filter(username=Username).exists():
                messages.error(request, "This Username already exists, please choose another name")
                return redirect('Admin_Register')

            if User.objects.filter(email=Email).exists():
                messages.error(request, "This E-Mail ID already exists, please choose another one")
                return redirect('Admin_Register')
            
            # Create user
            user = User.objects.create_user(username=Username, email=Email, password=Password)
            user.save()
            
            # Save profile image 
            if Profile_img:
                Profile.objects.create(user=user, profile_picture=Profile_img)

            messages.success(request, "Account created successfully!")
            return redirect('Admin_Login')
        except Exception as e:
                messages.error(request, f"Something went wrong: {str(e)}")
                return redirect('Admin_Register')

    return render(request,'dashboard/authentication/register.html')

# Admin Logout section
def admin_logout(request):
    auth.logout(request)
    messages.success(request, 'Successfully Logout!')
    return redirect('Admin_Login')

# Admin Dashboard Section
def admin_dashboard(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
        vehicle_data=Vehicles.objects.all()
    except Profile.DoesNotExist:
        user_profile = None
    # Paginator setting
    vehicle_queryset = Vehicles.objects.order_by('-created_at')
    page=Paginator(vehicle_queryset,2)
    page_number=request.GET.get('page')
    vehicle_list=page.get_page(page_number)
    context = {
        'data': user_profile,
        'vehicles':vehicle_data,
        'page_number':vehicle_list,
    }
    return render(request,'dashboard/index.html',context)

# Add Vehicle Section
def add_vehicle(request):
    new_vehicle = None 
    
    if request.method == "POST":
        try:
            vehicle_name = request.POST.get("vehicle_name")
            vehicle_short_title = request.POST.get("vehicle_short_title")
            vehicle_image = request.FILES.get("vehicle_image")
            vehicle_product_short_desc = request.POST.get("vehicle_product_short_desc")
            vehicle_range = request.POST.get("vehicle_range")
            vehicle_top_speed = request.POST.get("vehicle_top_speed")
            vehicle_motor_power = request.POST.get("vehicle_motor_power")
            vehicle_horsepower = request.POST.get("vehicle_horsepower")
            vehicle_torque = request.POST.get("vehicle_torque")
            vehicle_feature_1 = request.POST.get("vehicle_feature_1")
            vehicle_feature_2 = request.POST.get("vehicle_feature_2")
            vehicle_feature_3 = request.POST.get("vehicle_feature_3")
            vehicle_feature_4 = request.POST.get("vehicle_feature_4")
            vehicle_status = request.POST.get("vehicle_status") == "on"

            new_vehicle = Vehicles.objects.create(
                vehicle_name=vehicle_name,
                vehicle_short_title=vehicle_short_title,
                vehicle_image=vehicle_image,
                vehicle_product_short_desc=vehicle_product_short_desc,
                vehicle_range=vehicle_range,
                vehicle_top_speed=vehicle_top_speed,
                vehicle_motor_power=vehicle_motor_power,
                vehicle_horsepower=vehicle_horsepower,
                vehicle_torque=vehicle_torque,
                vehicle_feature_1=vehicle_feature_1,
                vehicle_feature_2=vehicle_feature_2,
                vehicle_feature_3=vehicle_feature_3,
                vehicle_feature_4=vehicle_feature_4,
                vehicle_status=vehicle_status
            )
            messages.success(request, "Vehicle added successfully!")
            return redirect("success_page")
        except Exception as e:
            messages.error(request, f"Error adding vehicle: {str(e)}")
            return redirect("add_vehicle")    
    
    context = {
        'vehicle_data': new_vehicle 
    }   
    
    return render(request, 'dashboard/vehicle_data/add_vehicle.html', context)
