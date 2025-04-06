from . import views
from django.urls import path


urlpatterns = [
    path('',views.admin_login,name="Admin_Login"),
    path('register/',views.admin_register,name="Admin_Register"),
    path('logout/',views.admin_logout,name="Admin_logout"),
    path('dashboard/',views.admin_dashboard,name="Admin_Dashboard"),
    path('add_vehicle/',views.add_vehicle,name="Add_Vehicle"),

    
]