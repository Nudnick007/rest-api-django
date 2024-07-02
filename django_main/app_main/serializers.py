from rest_framework import serializers
from app_main.models import Vendor, PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Vendor model.
    """
    Email = serializers.EmailField(allow_blank=True, required=False)
    Territory = serializers.CharField(allow_blank=True, required=False)
    IaAlertDays = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        model = Vendor
        fields = ('VendorNo', 'VendorName', 'Email', 'Email2', 'Email3', 'Email4', 'Territory', 'IaAlertDays')

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
