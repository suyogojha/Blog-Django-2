from django.db.models import fields
from blogapp.models import mobile, brand, Subscribe
from django import forms
from django.db import models


# class blogappForm(forms.Form):
#     name = models.CharField(max_length=255)
#     price = models.CharField(max_length=255)
#     code = models.CharField(max_length=255, null=True, blank=True)
#     storage = models.CharField(max_length=255, null=True, blank=True)
#     color = models.CharField(max_length=255, null=True, blank=True)
#     brand = models.ForeignKey(brand, on_delete=models.CASCADE, null=True, blank=True)
#     image = models.ImageField(upload_to="upload/image", null=True, blank=True)
#     description = models.TextField(max_length=255, null=True, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
    
    

class blogappForm(forms.ModelForm):
    class Meta:
        model = mobile
        fields = "__all__"
        

