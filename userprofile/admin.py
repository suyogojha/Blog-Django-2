from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from .models import profile

# Register your models here.
@admin.register(profile)
class UserprofileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name" , "address", "contact", "email")
    
    
