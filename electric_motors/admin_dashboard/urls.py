from . import views
from django.urls import path

app_name = "admin_dashboard"


urlpatterns = [
    path('',views.admin_login,name="Admin_Login"),
    path('register/',views.admin_register,name="Admin_Register"),
    path('logout/',views.admin_logout,name="Admin_logout"),
    path('dashboard/',views.admin_dashboard,name="Admin_Dashboard"),
    path('add_vehicle/', views.add_vehicle, name='Add_Vehicle'),
    path('edit_vehicle/<int:vehicle_id>/', views.edit_vehicle, name='Edit_Vehicle'),
    path('delete_vehicle/<int:vehicle_id>/', views.delete_vehicle, name='Delete_Vehicle'),
    path('get_user_data/', views.user_data, name='Get_User_Data'),
    
]