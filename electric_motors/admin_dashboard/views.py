from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages,auth
from django.contrib.auth.models import User
from . models import Profile
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from Product. models import *
from django.utils.timezone import now
import calendar

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
                messages.success(request, " Welcome, Admin! You've logged in successfully!")
                return redirect('admin_dashboard:Admin_Dashboard')
            else:
                auth.login(request, user)
                messages.success(request, f"Good to see you, {user.username}! You’ve successfully logged in!")
                return redirect('admin_dashboard:Admin_Dashboard')
        else:
            messages.error(request, 'Oops! That username or password doesn’t look right. Please try again.')
            return redirect('admin_dashboard:Admin_Login')    
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
                return redirect('admin_dashboard:Admin_Register')

            if User.objects.filter(username=Username).exists():
                messages.error(request, "This Username already exists, please choose another name")
                return redirect('admin_dashboard:Admin_Register')

            if User.objects.filter(email=Email).exists():
                messages.error(request, "This E-Mail ID already exists, please choose another one")
                return redirect('admin_dashboard:Admin_Register')
            
            # Create user
            user = User.objects.create_user(username=Username, email=Email, password=Password)
            user.save()
            
            # Save profile image 
            Profile.objects.create(user=user, profile_picture=Profile_img)

            messages.success(request, "Account creation complete! You’re ready to get started.")
            return redirect('admin_dashboard:Admin_Login')
        except Exception as e:
                messages.error(request, f"Something went wrong: {str(e)}")
                return redirect('admin_dashboard:Admin_Register')

    return render(request,'dashboard/authentication/register.html')

# Admin Logout section
@login_required(login_url='admin_dashboard:Admin_Login')
def admin_logout(request):
    auth.logout(request)
    messages.success(request, 'Goodbye! You’ve successfully logged out.')
    return redirect('admin_dashboard:Admin_Login')

# Admin Dashboard Section
@login_required(login_url='admin_dashboard:Admin_Login')
def admin_dashboard(request):
    # User name and Profile img 
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    
    # Paginator setting
    vehicle_queryset = Vehicles.objects.order_by('created_at')
    page=Paginator(vehicle_queryset,3)
    page_number=request.GET.get('page')
    vehicle_list=page.get_page(page_number)

    # Total vehicle Count get
    total_count=Vehicles.objects.count()

    # Customer Enquiries Count
      
    # calculate mounth count
    today=now()
    month=today.month
    year=today.year
    customer_count=Contact.objects.filter(created_at__year=year,created_at__month=month).count()
    # Month Name
    month_name=calendar.month_name[month]

    context = {
        'data': user_profile,
        'page_number':vehicle_list,
        'vehicle_count':total_count,
        'customer_count':customer_count,
        'month_name':month_name,
        'year':year
    }
    return render(request,'dashboard/index.html',context)

# Add Vehicle Section
@login_required(login_url='admin_dashboard:Admin_Login')
def add_vehicle(request):
    new_vehicle = None 
    
    if request.method == "POST":
        try:
            vehicle_name = request.POST.get("vehicle_name")
            vehicle_short_title = request.POST.get("vehicle_short_title")
            vehicle_image = request.FILES.get("vehicle_image")
            vehicle_product_short_desc = request.POST.get("vehicle_product_short_desc")
            vehicle_motor_type = request.POST.get("vehicle_motor_type")
            vehicle_range = request.POST.get("vehicle_range")
            vehicle_top_speed = request.POST.get("vehicle_top_speed")
            vehicle_motor_power = request.POST.get("vehicle_motor_power")
            vehicle_horsepower = request.POST.get("vehicle_horsepower")
            vehicle_torque = request.POST.get("vehicle_torque")
            vehicle_feature_1 = request.POST.get("vehicle_feature_1")
            vehicle_feature_2 = request.POST.get("vehicle_feature_2")
            vehicle_feature_3 = request.POST.get("vehicle_feature_3")
            vehicle_feature_4 = request.POST.get("vehicle_feature_4")
            vehicle_status = True if request.POST.get("vehicle_status") == "on" else False

            new_vehicle = Vehicles.objects.create(
                vehicle_name=vehicle_name,
                vehicle_short_title=vehicle_short_title,
                vehicle_image=vehicle_image,
                vehicle_product_short_desc=vehicle_product_short_desc,
                vehicle_motor_type=vehicle_motor_type,
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
            messages.success(request, "Vehicle has been successfully added!")
            return redirect("admin_dashboard:Admin_Dashboard")
        except Exception as e:
            messages.error(request, f"Error adding vehicle: {str(e)}")
            return redirect("admin_dashboard:Add_Vehicle")    
    
    context = {
        'vehicle_data': new_vehicle 
    }   
    return render(request,'dashboard/vehicle_data/add_vehicle.html', context)

#  Edit Vehicle data 
@login_required(login_url='admin_dashboard:Admin_Login')
def edit_vehicle(request,vehicle_id):
    get_vehicle=get_object_or_404(Vehicles,vehicle_id=vehicle_id)

    if request.method=='POST':
        try:
            get_vehicle.vehicle_name = request.POST.get("vehicle_name")
            get_vehicle.vehicle_short_title = request.POST.get("vehicle_short_title")
            get_vehicle.vehicle_product_short_desc = request.POST.get("vehicle_product_short_desc")
            get_vehicle.vehicle_motor_type = request.POST.get("vehicle_motor_type")
            get_vehicle.vehicle_range = request.POST.get("vehicle_range")
            get_vehicle.vehicle_top_speed = request.POST.get("vehicle_top_speed")
            get_vehicle.vehicle_motor_power = request.POST.get("vehicle_motor_power")
            get_vehicle.vehicle_horsepower = request.POST.get("vehicle_horsepower")
            get_vehicle.vehicle_torque = request.POST.get("vehicle_torque")
            get_vehicle.vehicle_feature_1 = request.POST.get("vehicle_feature_1")
            get_vehicle.vehicle_feature_2 = request.POST.get("vehicle_feature_2")
            get_vehicle.vehicle_feature_3 = request.POST.get("vehicle_feature_3")
            get_vehicle.vehicle_feature_4 = request.POST.get("vehicle_feature_4")
            get_vehicle.vehicle_status = True if request.POST.get("vehicle_status") == "on" else False

            if "vehicle_image" in request.FILES:
                get_vehicle.vehicle_image = request.FILES["vehicle_image"]

            get_vehicle.save()
            messages.success(request, "Vehicle record has been updated successfully.")
            return redirect("admin_dashboard:Admin_Dashboard")
        except Exception as e:
            messages.error(request, f"Error updating vehicle: {str(e)}")
            return redirect("admin_dashboard:Edit_Vehicle", vehicle_id=vehicle_id)
    context = {
        "edit_vehicle": get_vehicle
    }
    return render(request, 'dashboard/vehicle_data/edit_vehicle.html', context)

#  Delete Vehicle Data
@login_required(login_url='admin_dashboard:Admin_Login')
def delete_vehicle(request,vehicle_id):
    get_vehicle_data=Vehicles.objects.get(vehicle_id=vehicle_id)
    get_vehicle_data.delete()
    return redirect("admin_dashboard:Admin_Dashboard")

# Get User Enquiry for Vehicle
@login_required(login_url='admin_dashboard:Admin_Login')
def user_data(request):
    get_user_data=Contact.objects.all()

    context={
        'user_data':get_user_data
    }

    return render(request, 'dashboard/get_user_data.html', context)

# Setting
@login_required(login_url='admin_dashboard:Admin_Login')
def setting(request):
    return render(request,'dashboard/404_page.html')

# help_center
@login_required(login_url='admin_dashboard:Admin_Login')
def help_center(request):
    return render(request,'dashboard/404_page.html')

# Change User password
@login_required(login_url='admin_dashboard:Admin_Login')
def change_password(request):
    # currently logged-in user
    user = request.user

    # data get
    if request.method == 'POST':
        Current_password = request.POST.get('current_password')
        New_password = request.POST.get('new_password')
        Confirm_password = request.POST.get('confirm_password')

        # Current Password checking
        if not user.check_password(Current_password):
            messages.error(request, "Oops! The password you entered is invalid. Please check and try again.")
            return redirect('admin_dashboard:Change_Password') 
        
        # New and Confirm Password does not match
        if New_password != Confirm_password:
            messages.error(request, "Oops! Your new password and confirm password don't match. Please re-check them.")
            return redirect('admin_dashboard:Change_Password')
        
        user.set_password(New_password)
        user.save()
        messages.success(request, "Your password has been updated. Please log in again to continue.")
        return redirect('admin_dashboard:Admin_Login')

    return render(request,'dashboard/authentication/change_password.html')
        