from rest_framework import serializers
from app_main.models import Vendor, PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Vendor model.
    """
    class Meta:
        model = Vendor
        fields = ('VendorNo', 'VendorName', 'Email', 'Territory', 'IaAlertDays')

class PurchaseOrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the PurchaseOrder model.

    VendorNo:
    - Represents the foreign key to the Vendor model using its primary key.
    - Validates that the provided VendorNo exists in the Vendor queryset.
    """
    VendorNo = serializers.PrimaryKeyRelatedField(queryset=Vendor.objects.all())
    
    class Meta:
        model = PurchaseOrder
        fields = ('PONO', 'VendorNo', 'ShipDate', 'Customer', 'IaSubmissionDate', 'InspectionDate')
