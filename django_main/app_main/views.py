from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from app_main.models import Vendor, PurchaseOrder
from app_main.serializers import VendorSerializer, PurchaseOrderSerializer
from django.contrib import messages
from django.http import HttpResponse
from .forms import DetailsForm
from .models import document

@csrf_exempt
def vendorApi(request, id=0):
    """
    API endpoint for handling CRUD operations on Vendor objects.
    """
    if request.method == "GET":
        try:
            # Retrieve all Vendor objects
            vendors = Vendor.objects.all()
            # Serialize the queryset
            vendors_serializer = VendorSerializer(vendors, many=True)
            # Return JSON response with serialized data
            return JsonResponse(vendors_serializer.data, safe=False)
        except Exception as e:
            # Return JSON response with error message if an exception occurs
            return JsonResponse({"error": str(e)}, safe=False)

    elif request.method == "POST":
        try:
            # Parse JSON data from request
            vendor_data = JSONParser().parse(request)
            # Initialize serializer with parsed data
            vendors_serializer = VendorSerializer(data=vendor_data)
            if vendors_serializer.is_valid():
                # Save valid serializer data to database
                vendors_serializer.save()
                # Return success message
                return JsonResponse("Added Successfully", safe=False)
            # Return error message if serializer data is invalid
            return JsonResponse("Failed to Add", safe=False)
        except Exception as e:
            # Return JSON response with error message if an exception occurs
            return JsonResponse({"error": str(e)}, safe=False)

    elif request.method == "PUT":
        try:
            # Parse JSON data from request
            vendor_data = JSONParser().parse(request)
            # Retrieve Vendor object to update
            vendor = Vendor.objects.get(VendorNo=vendor_data['VendorNo'])
            # Initialize serializer with instance and parsed data
            vendors_serializer = VendorSerializer(vendor, data=vendor_data)
            if vendors_serializer.is_valid():
                # Save valid serializer data to update the instance
                vendors_serializer.save()
                # Return success message
                return JsonResponse("Updated Successfully", safe=False)
            # Return error message if serializer data is invalid
            return JsonResponse("Failed to Update", safe=False)
        except Vendor.DoesNotExist:
            # Return error message if Vendor with specified VendorNo does not exist
            return JsonResponse("Vendor Not Found", safe=False)
        except Exception as e:
            # Return JSON response with error message if an exception occurs
            return JsonResponse({"error": str(e)}, safe=False)

    elif request.method == "DELETE":
        try:
            # Retrieve Vendor object to delete
            vendor = Vendor.objects.get(VendorNo=id)
            # Delete the retrieved Vendor object
            vendor.delete()
            # Return success message
            return JsonResponse("Deleted Successfully", safe=False)
        except Vendor.DoesNotExist:
            # Return error message if Vendor with specified VendorNo does not exist
            return JsonResponse("Vendor Not Found", safe=False)
        except Exception as e:
            # Return JSON response with error message if an exception occurs
            return JsonResponse({"error": str(e)}, safe=False)

@csrf_exempt
def purchaseorderApi(request, id=0):
    """
    API endpoint for handling CRUD operations on PurchaseOrder objects.
    """
    if request.method == "GET":
        try:
            # Retrieve all PurchaseOrder objects
            purchaseorders = PurchaseOrder.objects.all()
            # Serialize the queryset
            purchaseorders_serializer = PurchaseOrderSerializer(purchaseorders, many=True)
            # Return JSON response with serialized data
            return JsonResponse(purchaseorders_serializer.data, safe=False)
        except Exception as e:
            # Return JSON response with error message if an exception occurs
            return JsonResponse({"error": str(e)}, safe=False)

    elif request.method == "POST":
        try:
            # Parse JSON data from request
            purchaseorder_data = JSONParser().parse(request)
            # Initialize serializer with parsed data
            purchaseorders_serializer = PurchaseOrderSerializer(data=purchaseorder_data)
            if purchaseorders_serializer.is_valid():
                # Save valid serializer data to database
                purchaseorders_serializer.save()
                # Return success message
                return JsonResponse("Added Successfully", safe=False)
            # Return error message if serializer data is invalid
            return JsonResponse("Failed to Add", safe=False)
        except Exception as e:
            # Return JSON response with error message if an exception occurs
            return JsonResponse({"error": str(e)}, safe=False)

    elif request.method == "PUT":
        try:
            # Parse JSON data from request
            purchaseorder_data = JSONParser().parse(request)
            # Retrieve PurchaseOrder object to update
            purchaseorder = PurchaseOrder.objects.get(PONO=purchaseorder_data['PONO'])
            # Initialize serializer with instance and parsed data
            purchaseorders_serializer = PurchaseOrderSerializer(purchaseorder, data=purchaseorder_data)
            if purchaseorders_serializer.is_valid():
                # Save valid serializer data to update the instance
                purchaseorders_serializer.save()
                # Return success message
                return JsonResponse("Updated Successfully", safe=False)
            # Return error message if serializer data is invalid
            return JsonResponse("Failed to Update", safe=False)
        except PurchaseOrder.DoesNotExist:
            # Return error message if PurchaseOrder with specified PONO does not exist
            return JsonResponse("Purchase Order Not Found", safe=False)
        except Exception as e:
            # Return JSON response with error message if an exception occurs
            return JsonResponse({"error": str(e)}, safe=False)

    elif request.method == "DELETE":
        try:
            # Retrieve PurchaseOrder object to delete
            purchaseorder = PurchaseOrder.objects.get(PONO=id)
            # Delete the retrieved PurchaseOrder object
            purchaseorder.delete()
            # Return success message
            return JsonResponse("Deleted Successfully", safe=False)
        except PurchaseOrder.DoesNotExist:
            # Return error message if PurchaseOrder with specified PONO does not exist
            return JsonResponse("Purchase Order Not Found", safe=False)
        except Exception as e:
            # Return JSON response with error message if an exception occurs
            return JsonResponse({"error": str(e)}, safe=False)

def home(request):
    return render(request, "index.html")

def upload_file(request):
    if request.method == "POST":
        form = DetailsForm(request.POST, request.FILES)
        if form.is_valid():
            # If multiple files are uploaded, iterate through them
            for file in request.FILES.getlist('files'):
                # Create a new instance of DetailsForm for each file
                form = DetailsForm(request.POST, {'DocName': file.name, 'Doc': file})
                if form.is_valid():
                    form.save()
            
            return redirect('upload_success')  
    else:
        form = DetailsForm()
    return render(request, 'upload.html', {'form': form})