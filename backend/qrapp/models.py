from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class CodeStatus(models.TextChoices):
    Initial = 'initial'
    Printed = 'printed'
    Discarded = 'discarded'
    Completed = 'completed'

class QRCode(models.Model):
    uuid = models.UUIDField( unique=True, default= uuid.uuid4, max_length=32, editable=False)

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='qrcodes'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    printed_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=16, choices=CodeStatus.choices, default= CodeStatus.Initial, help_text="Status of a QR code")
    
    
    class Meta:
        ordering = ['created_at']


class BarCode(models.Model):    
    created_at = models.DateTimeField(auto_now_add=True)
    printed_at = models.DateTimeField(null=True)
    
    status = models.CharField(max_length=16, choices=CodeStatus.choices, default= CodeStatus.Initial, help_text="Status of a Bar code")

        
    class Meta:
        ordering = ['created_at']
        
        
    def __str__(self) -> str:
        return f"{self.uid}"
    
        
        
class TrayStatus(models.TextChoices):
    Initial = 'initial'
    InStorage = 'in-storage'
    InPackage = 'in-package'
    Discarded = 'discarded'
    Completed = 'completed'
        
class TrayWithCode(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    in_storage_at = models.DateTimeField(null=True)
    in_package_at = models.DateTimeField(null=True)
    discarded_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)
    
    qrcode = models.ForeignKey(QRCode, null= False, on_delete=models.CASCADE,
                                            related_name= 'tray' )
    barcode = models.ForeignKey(BarCode, null= False, on_delete=models.CASCADE,
                                            related_name= 'tray' )
    
    status = models.CharField(max_length=16, choices=TrayStatus.choices, default= TrayStatus.Initial, help_text="Status of a tray")
    
    
class Printer(models.Model):
    name = models.CharField(max_length=100, help_text="printer name")
    active = models.BooleanField(default=True)
    
    
    def __str__(self) -> str:
        return self.name