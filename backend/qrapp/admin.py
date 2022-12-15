from django.contrib import admin
from .models import QRCode, BarCode, TrayWithCode, Printer
# Register your models here.
class QRCodeAdmin(admin.ModelAdmin):

    list_display = ( 'creator',  'printed_at')
    readonly_fields = ('uuid', 'created_at' )
    

class BarCodeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(QRCode, QRCodeAdmin)
admin.site.register(BarCode, BarCodeAdmin)
admin.site.register(TrayWithCode)
admin.site.register(Printer)