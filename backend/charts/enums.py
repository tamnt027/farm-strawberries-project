from django.db import models
from enum import Enum as MyEnum
    
class ChartType(models.TextChoices):
    Scatter = 'scatter'
    
    
class ChartMode(models.TextChoices):
    Lines = 'lines'
    

class ChartYAxis(models.TextChoices):
    yaxis1 =  'y1'
    yaxis2 =  'y2'
    
    
class ChartTimeRange(models.TextChoices):
    Last1H = '1h'
    Last6H = '6h'
    Last12H = '12h'
    Last1D = '1d'
    Last3D = '3d'
    Last1W = '1w'
    Last2W = '2w'
    Last1M = '1mo'
    Last3M = '3mo'
    Last6M = '6mo'
    Last1Y = '1y'