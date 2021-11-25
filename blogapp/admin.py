from django.contrib import admin
from .models import mobile, brand, Subscribe

# Register your models here.


@admin.register(mobile)
class mobileAdmin(admin.ModelAdmin):
    list_display = ("person", "name", "price", "code", "storage", "color", "brand", "description", "created", "modified", "created_by")
    list_filter = ("price",)
    search_fields = ["name"]



@admin.register(brand)
class brandAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "location")
    

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ("email",)
