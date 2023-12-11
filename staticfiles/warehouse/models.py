# models.py

from django.db import models
from django.utils.html import mark_safe
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=255)
   
    
    def __str__(self):
        return f'{self.name}'

class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.name} - {self.location}'

class Coding(models.Model):    
    coding =  models.CharField(max_length=50)
    details = models.CharField(max_length=125, null=True, blank=True)
    
    def __str__(self):
        return f'{self.coding}'



class Items(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    coding = models.ForeignKey(Coding, on_delete=models.CASCADE) 
    stockname = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    critical = models.PositiveIntegerField(default=0)
 
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def display_image_thumbnail(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" style="max-height: 50px; max-width: 50px;" />')
        return None
    
    def __str__(self):
        return f'{self.stockname} '
    
class CompanyRec(models.Model):
    company = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contactperson =models.CharField(max_length=150)
    contactnumber=models.CharField(max_length=50)
    email=models.EmailField(null=True,blank=True)
    def __str__(self):
        return f'{self.company} - {self.contactnumber}'
    
class Transaction(models.Model):
    item =models.ForeignKey(Items, on_delete=models.CASCADE)  
    transdate =models.DateTimeField(default=timezone.now,blank=True)
    docnumber =models.CharField(max_length=100,null=True, blank=True)
    qtyIN = models.DecimalField(default=0, max_digits=5,decimal_places=2)
    qtyout = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)  
    company = models.ForeignKey(CompanyRec, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.transdate} {self.item} - {self.warehouse}'
    
