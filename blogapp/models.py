from django.db import models
from django.db.models.fields.related import ForeignKey
from userprofile .models import User

# Create your models here.

class brand(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name


class mobile(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)
    storage = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="upload/image", null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    person = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

 



class Subscribe(models.Model):
    email = models.CharField(max_length=255, null=True, blank=True)    
    
    
    def __str__(self):
        return self.name
