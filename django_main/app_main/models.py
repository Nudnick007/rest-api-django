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

    def __str__(self):
        return self.VendorNo
    
@receiver(pre_save, sender=Vendor)
def set_default_password(instance, **kwargs):
    if not instance.Password:
        instance.Password = instance.VendorNo

class PurchaseOrder(models.Model):
    PONO = models.CharField(max_length = 255,primary_key=True)
    VendorNo = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    # VendorName = models.ForeignKey('Vendor', to_field='VendorName', on_delete=models.CASCADE, related_name='purchase_orders_vendorname',null=True,unique=True)
    ShipDate = models.DateField()
    Customer = models.CharField(max_length=255)
    IaSubmissionDate = models.DateField(null=True) 
    InspectionDate = models.DateField(null=True)
    InspectionDateProposed = models.DateField(null=True)
    Status = models.CharField(default="Inspection date to be submitted")
    Alerts = models.CharField(null=True)
    username = models.ForeignKey('users', on_delete=models.CASCADE,null=True)
    vendoralerts = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.PONO

class document(models.Model):
    Id = models.AutoField(primary_key=True)
    DocName = models.TextField(max_length=255,null=True)
    Doc = models.FileField(upload_to="files",blank=True,null=True)
    DocType = models.CharField(max_length=255,null=True)
    PONO = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE,null=True)
    VendorNo = models.ForeignKey('Vendor', on_delete=models.CASCADE,null=True)
    Convention = models.CharField(max_length=255, null=True, blank=True)
    Date = models.DateField(auto_now_add=True,null=True)

    def save(self, *args, **kwargs):
        if self.VendorNo and self.PONO and self.DocType:
            base_convention = f"{self.VendorNo}-{self.PONO}-{self.DocType}"
            self.Convention = base_convention

            existing_documents = document.objects.filter(Convention__startswith=base_convention)
            if existing_documents.exists():
                max_suffix = 0
                for doc in existing_documents:
                    convention = doc.Convention
                    if convention == base_convention:
                        suffix = 1
                    else:
                        try:
                            suffix = int(convention[len(base_convention)+1:])
                        except ValueError:
                            continue
                    if suffix > max_suffix:
                        max_suffix = suffix
                new_suffix = max_suffix + 1
                self.Convention = f"{base_convention}-{new_suffix}"

        super().save(*args, **kwargs)

class users(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('qa', 'Qa'),
    ]
    username = models.CharField(max_length=255,primary_key=True)
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='user')
    password = models.CharField(max_length=500)
    email = models.EmailField(default="",blank=True)
    

