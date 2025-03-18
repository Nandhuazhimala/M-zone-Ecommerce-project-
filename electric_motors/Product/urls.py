from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name="Home_Page"),
    path('about_us/',views.about,name="About_Us"),
    path('latestt_vehicles/',views.vehicles,name="Latest_Vehicles"),
    path('vehicle_detail/',views.vehicle_data,name="Vehicles_Data"),
    path('contact_us/',views.contact,name="Contact_Us"),
    path('news_slidbar/',views.news,name="News_Slidbar"),
    path('blog_data/',views.blog,name="Blog_Data"),
]