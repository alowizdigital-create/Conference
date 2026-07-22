from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create/", company_create, name="product_create"),
    path("categories/", category_list, name="category_list"),
    path("categories/create/", category_create, name="category_create"),
  
]
