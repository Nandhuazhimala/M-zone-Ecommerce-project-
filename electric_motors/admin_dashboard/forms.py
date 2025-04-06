from django import forms
from Product.models import *

class VehiclelForm(forms.ModelForm):
    model = Vehicles
    fields = ['vehicle_name','vehicle_short_title','vehicle_image','vehicle_product_short_desc',
              'vehicle_product_desc','vehicle_range','vehicle_top_speed','vehicle_motor_power',
              'vehicle_horsepower','vehicle_torque','vehicle_feature_1','vehicle_feature_2',
              'vehicle_feature_3','vehicle_feature_4','vehicle_status']
