from django.urls import path
from .views import blogapp, about, add_product, edit_product, delete_product, details, created_by_user, storage, usercreated, storage1



app_name = "blogapp"



urlpatterns = [
    path('index/', blogapp, name="blogapp"),
    path('about/', about, name="about"),
    path('details/', details, name="details"),
    path('usercreated/', usercreated, name="usercreated"),
    path('created_by/', created_by_user, name="created_by_user"),
    path('storage/', storage, name="storage"),
    path('storage1/', storage1, name="storage1"),
    path('add_product/', add_product, name="add_product"),
    path('edit_product/<int:product_id>', edit_product, name="edit_product"),
    path('delete_product/<int:product_id>', delete_product, name="delete_product"),
    
]
