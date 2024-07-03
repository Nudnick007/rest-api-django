from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Vendor(models.Model):
    VendorNo = models.CharField(max_length=255,primary_key=True)
    VendorName = models.CharField(max_length=500)
    Email = models.EmailField(default="",blank=True)
    Email2 = models.EmailField(null=True)
    Email3 = models.EmailField(null=True)
    Email4 = models.EmailField(null=True)
    Territory = models.CharField(null=True,max_length=255)
    IaAlertDays = models.IntegerField(null=True)
    Password = models.CharField(max_length=255, editable=False, blank=True)
    
@receiver(pre_save, sender=Vendor)
def set_default_password(instance, **kwargs):
    if not instance.Password:
        instance.Password = instance.VendorNo

class PurchaseOrder(models.Model):
    PONO = models.CharField(max_length = 255,primary_key=True)
    VendorNo = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    ShipDate = models.DateField()
    Customer = models.CharField(max_length=255)
    IaSubmissionDate = models.DateField(null=True) 
    InspectionDate = models.DateField(null=True)
    InspectionDateProposed = models.DateField(null=True)
    Status = models.CharField(default="Inspection date to be submitted")
    Alerts = models.CharField(null=True)

class document(models.Model):
    Id = models.AutoField(primary_key=True)
    DocName = models.CharField(max_length=255)
    Doc = models.FileField(upload_to="files",blank=True,null=True)
    DocType = models.CharField(max_length=255,null=True)
    PONO = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE,null=True)