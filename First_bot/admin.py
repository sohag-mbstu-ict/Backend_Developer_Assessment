from django.contrib import admin

# Register your models here.
from .models import Product,ProductDescription
admin.site.register(Product)
admin.site.register(ProductDescription)


