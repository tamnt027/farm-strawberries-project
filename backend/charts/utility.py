import asyncio
from .models import ChartGroup, LoraMeasurement, LoraDevice, Chart, SeriesDisplay
from .influxdb_helper import InfluxDbHelper
import logging
from cachetools import cached,  TTLCache

def import_chart_group_from_influxdb():
    recent_applications = InfluxDbHelper.get_instance().get_all_application_names()
    
    existed_chart_groups = ChartGroup.objects.all()
    existed_chart_group_names = [chart_group.name for chart_group in existed_chart_groups]
    for recent_app in recent_applications:
        if recent_app not in existed_chart_group_names:
            new_chart_group = ChartGroup(name=recent_app)
            new_chart_group.save()
            logging.info(f"Add new chart group {recent_app} to database")
    
    
def import_measurements_from_influxdb():
    recent_measurements = InfluxDbHelper.get_instance().get_all_measurements()
    saved_measurements = LoraMeasurement.objects.all()
    saved_measurements_names = [measurement.name for measurement in saved_measurements]
    for recent_measurement in recent_measurements:
        if recent_measurement not in saved_measurements_names:
            new_measurement_object = LoraMeasurement(name=recent_measurement)
            new_measurement_object.save()
            logging.info(f"Add new measurement {recent_measurement} to database")
    
def import_devices_from_influxdb():
    recent_devices_ids = InfluxDbHelper.get_instance().get_all_device_ids()
    saved_devices = LoraDevice.objects.all()
    saved_devices_ids = [device.device_id for device in saved_devices]
    for recent_device in recent_devices_ids:
        if recent_device not in saved_devices_ids:
            new_device_object = LoraDevice(name=recent_device, device_id=recent_device)
            new_device_object.save()
            logging.info(f"Add new device id {recent_device} to database")
            
            
def get_filters_by_chart_group(group_id:int):
    chart_group = ChartGroup.objects.get(pk=group_id)
    charts = chart_group.charts.all()
    chart : Chart
    
    filters = []
    
    for chart in charts:
        serial_displayes = chart.series_displays.all()
        serial_display : SeriesDisplay
        for serial_display in serial_displayes:
            device_eui = serial_display.device.device_id
            measurement = serial_display.measurement.name
            application = chart_group.name
            filters.append((device_eui, measurement, application))
            
    return filters
            
            
@cached(cache=TTLCache(maxsize=100, ttl=10))            
def get_charts_data_from_influxdb(group_id : int, period, time_range):
    filters = get_filters_by_chart_group(group_id)
    return InfluxDbHelper.get_instance().get_history_data_by_filters(filters, period, time_range)
    
            
def get_history_data( measurement, dev_eui, application, group_id,  period='60m', time_range="72h"):
    charts_data = get_charts_data_from_influxdb(group_id, period, time_range)
    # print(charts_data)
    for data in charts_data:
        if data["measurement"] == measurement and data["dev_eui"] == dev_eui and data["application_name"] == application:
            return (data["timestamps"], data["values"])
    return ([], [])
