# Create your models here.
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=750)
    
    def __str__(self):
        return self.name


class ProductDescription(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    genre = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title