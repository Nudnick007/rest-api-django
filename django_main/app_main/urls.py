from django.urls import re_path as url
from django.urls import path
from app_main import views
from app_main.views import upload_file
from django.shortcuts import render

urlpatterns = [
    # URL pattern for handling GET and POST requests related to vendors
    url(r'^vendor$', views.vendorApi),
    
    # URL pattern for handling GET, PUT, and DELETE requests related to a specific vendor identified by ID
    url(r'^vendor/([0-9]+)$', views.vendorApi),
    
    # URL pattern for handling GET and POST requests related to purchase orders
    url(r'^purchaseorder$', views.purchaseorderApi),
    
    # URL pattern for handling GET, PUT, and DELETE requests related to a specific purchase order identified by ID
    url(r'^purchaseorder/([0-9]+)$', views.purchaseorderApi),

    path("", views.home,name="home"),

    path("upload/", upload_file,name="upload"),
    path('upload/success/', lambda request: render(request, 'upload_success.html'), name='upload_success'),
]
