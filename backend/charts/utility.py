import asyncio
from .models import ChartGroup, LoraMeasurement, LoraDevice
from .influxdb_helper import InfluxDbHelper
import logging

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