from django.db import models
from colorfield.fields import ColorField
import datetime
from django.core.validators import MinValueValidator
from .enums import ChartMode, ChartType, ChartYAxis

class ChartGroup(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=256, null=True)
    
    def __str__(self) -> str:
        return f"{self.id}. {self.name}"

class LoraDevice(models.Model):
    name = models.CharField(max_length=100, default="", null=False)
    device_id = models.CharField(max_length=50, unique=True, null=False, 
                                 help_text="Dev UID")
    description = models.CharField(max_length=256, null=True)
    
    def __str__(self) -> str:
        return f"{self.name} ({self.id})"

class LoraMeasurement(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=256, null=True)

    def __str__(self) -> str:
        return f"{self.id}. {self.name}"
    
class SeriesDisplay(models.Model):
    name = models.CharField(max_length=32, null=False)
    mode = models.CharField(max_length=16, choices=ChartMode.choices, default= ChartMode.Lines, help_text="Chart mode")
    chart_type = models.CharField(max_length=16, choices=ChartType.choices, default= ChartType.Scatter, help_text="Chart type")
    color = ColorField(default='#0000FF', format="hexa", null=False)
    yaxis = models.CharField(max_length=10, null=False, choices= ChartYAxis.choices, default=ChartYAxis.yaxis1, help_text="Y axis 1 for left, Y axis 2 for right" )
    device = models.ForeignKey(LoraDevice, null= False,  default=0, on_delete=models.CASCADE, related_name= 'series' )
    measurement = models.ForeignKey(LoraMeasurement, null= False, default=0, on_delete=models.CASCADE, related_name= 'series' )
  
    def __str__(self):
        return f"{self.id}. {self.name}"
    
    
class Chart(models.Model):
    name = models.CharField(max_length=100, null=False)
    title = models.CharField(max_length=256, null=True)
    display_priority = models.PositiveSmallIntegerField(default=0, 
                        help_text="Smaller value has higher priority to appear")
    title_size =  models.IntegerField(default=20, null=False, 
                        validators=[MinValueValidator(8)], help_text="Title font size")
    title_color = ColorField(default='#000000', format="hexa", help_text="Title color")
    created_date = models.DateTimeField(default= datetime.datetime.now, editable=False)
    active = models.BooleanField(default=True, 
                                 help_text="Uncheck to prevent displaying")
    series_displays = models.ManyToManyField(SeriesDisplay,  blank=True,
                                             related_name="in_charts")
    group = models.ForeignKey(ChartGroup, null= False, on_delete=models.CASCADE,
                                            related_name= 'charts' )
    
    def __str__(self):
        return f"{self.id}. {self.name}"