from django.contrib import admin
from .models import *
from django import forms


# Register your models here.
admin.site.register(Product)
admin.site.register(Warehouse)

admin.site.register(Coding)
class ProductAdmin(admin.ModelAdmin):
    
    search_fields = ['stockname', 'description']
    list_display = ('stockname', 'description', 'coding', 'display_image_thumbnail')

    def display_image_thumbnail(self, obj):
        return obj.display_image_thumbnail()

    display_image_thumbnail.short_description = 'Image'

admin.site.register(Items, ProductAdmin)

admin.site.register(Transaction)

admin.site.register(CompanyRec)



