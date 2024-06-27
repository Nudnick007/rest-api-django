from django.urls import re_path as url
from app_main import views

urlpatterns = [
    # URL pattern for handling GET and POST requests related to vendors
    url(r'^vendor$', views.vendorApi),
    
    # URL pattern for handling GET, PUT, and DELETE requests related to a specific vendor identified by ID
    url(r'^vendor/([0-9]+)$', views.vendorApi),
    
    # URL pattern for handling GET and POST requests related to purchase orders
    url(r'^purchaseorder$', views.purchaseorderApi),
    
    # URL pattern for handling GET, PUT, and DELETE requests related to a specific purchase order identified by ID
    url(r'^purchaseorder/([0-9]+)$', views.purchaseorderApi),
]
