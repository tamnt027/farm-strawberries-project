from django.contrib import admin
from .models import LoraMeasurement, Chart, LoraDevice, SeriesDisplay, ChartGroup
# Register your models here.
admin.site.register(LoraMeasurement)
admin.site.register(LoraDevice)
admin.site.register(ChartGroup)
admin.site.register(Chart)
admin.site.register(SeriesDisplay)