# Create your models here.
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=750,default="")
    link=models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    


class ProductDescription(models.Model):
    
    name = models.CharField(max_length=750,blank=True, null=True)

    availability=models.CharField(max_length=15,blank=True, null=True)

    rating=models.CharField(max_length=15 ,default=0,blank=True, null=True)

    total_rating=models.CharField(max_length=20 ,default=0,blank=True, null=True)

    price=models.CharField(max_length=15 ,default=0,blank=True, null=True)

    shipping_import_details=models.CharField(max_length=100,default="",blank=True, null=True)

    delivery=models.CharField(max_length=30,blank=True, null=True)

    brand=models.CharField(max_length=20,blank=True, null=True)

    connectivity_technology=models.CharField(max_length=20,blank=True, null=True)

    connector_type=models.CharField(max_length=30,blank=True, null=True)

    compatible_device=models.TextField(max_length=500,blank=True, null=True)

    compatible_models=models.TextField(max_length=700,blank=True, null=True)

    # special_features=models.TextField(max_length=300,blank=True, null=True)

    # color=models.CharField(max_length=15,blank=True, null=True)

    # input_voltage=models.CharField(max_length=15,blank=True, null=True)

    # mounting_type=models.CharField(max_length=50,blank=True, null=True)

    about_this_item=models.TextField(max_length=2000,blank=True, null=True)

    genre = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name