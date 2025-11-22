from django.db import models
from django.contrib import admin
class Product(models.Model):
    productID=models.CharField(primary_key=True,max_length=30)
    name=models.CharField(max_length=20)
    listing_date=models.DateTimeField()
    price=models.IntegerField()
    sellerID=models.CharField(max_length=30)
    quantity=models.IntegerField()
    category=models.CharField(max_length=20)

class ProductAdmin(admin.ModelAdmin):
    list_display=["productID","name","listing_date","price","sellerID","quantity","category"]
