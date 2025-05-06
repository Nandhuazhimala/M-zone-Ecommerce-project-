from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
# class BannerSection(models.Model):
#     BANNER_CHOICES=[
#         ('HOME_BANNER','Home_Banner'),
#         ('OTHER_banner','Other_Banner')
#     ]
#     name=models.CharField(max_length=100,choices=BANNER_CHOICES)
#     home_banner_bg=models.ImageField(upload_to='homapage_banner_background', null=True, blank=True)
#     product_logo=models.ImageField(upload_to='Logo', null=True, blank=True)
#     def __str__(self):
#         return self.name
    
class Vehicles(models.Model):
    # banner = models.ForeignKey(BannerSection, related_name='banner_section', on_delete=models.CASCADE)
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_name=models.CharField(max_length=25)
    vehicle_short_title=models.CharField(max_length=255,null=True)
    vehicle_image=models.ImageField(upload_to='vehicle_image')
    vehicle_product_short_desc = models.CharField(max_length=255,null=True)
    vehicle_product_desc = models.TextField(default=None, null=True)
    vehicle_motor_type = models.CharField(max_length=255,null=True)
    vehicle_range = models.IntegerField(validators=[MinValueValidator(0)])
    vehicle_top_speed = models.IntegerField(validators=[MinValueValidator(0)])
    vehicle_motor_power = models.IntegerField(validators=[MinValueValidator(0)])
    vehicle_horsepower = models.IntegerField(validators=[MinValueValidator(0)])
    vehicle_torque = models.IntegerField(validators=[MinValueValidator(0)])
    vehicle_feature_1 = models.TextField()
    vehicle_feature_2 = models.TextField()
    vehicle_feature_3 = models.TextField()
    vehicle_feature_4 = models.TextField()
    vehicle_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vehicle_name
    
class Contact(models.Model):
    name= models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# class VehicleVariant(models.Model):
#     vehicle_variant_id = models.AutoField(primary_key=True)
#     vehicle = models.ForeignKey(Vehicles, related_name='Vehicles_datas', on_delete=models.CASCADE)
#     variant_img = models.ImageField(upload_to='vehicles/', max_length=100)
#     variant_price = models.DecimalField(max_digits=10, decimal_places=2)
#     name = models.CharField(max_length=100, blank=True, null=True)  # Optional name field