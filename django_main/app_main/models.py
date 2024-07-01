from django.db import models

# Create your models here.

class Vendor(models.Model):
    VendorNo = models.CharField(max_length=255,primary_key=True)
    VendorName = models.CharField(max_length=500)
    Email = models.EmailField()
    Territory = models.CharField(max_length=255)
    IaAlertDays = models.IntegerField()

class PurchaseOrder(models.Model):
    PONO = models.CharField(max_length = 255,primary_key=True)
    VendorNo = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    ShipDate = models.DateField()
    Customer = models.CharField(max_length=255)
    IaSubmissionDate = models.DateField() 
    InspectionDate = models.DateField()
    doc=models.FileField

class document(models.Model):
    Id = models.AutoField(primary_key=True)
    DocName = models.CharField(max_length=255)
    Doc = models.FileField(upload_to="app_main/files/",blank=True,null=True)
    DocType = models.CharField(max_length=255,null=True)
    PONO = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE,null=True)