from datetime import timedelta
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import logging
import typing
from cachetools import cached,  TTLCache
from decouple import config


def get_history_data_query_string(bucket, time_range, measurement,  application,  period,  dev_eui):
    query_string = f"""from(bucket: "{bucket}")
    |> range(start: -{time_range})
    |> filter(fn: (r) => r["_measurement"] == "{measurement}")
    |> filter(fn: (r) => r["_field"] == "value")
    |> filter(fn: (r) => r["dev_eui"] == "{dev_eui}")
    |> filter(fn: (r) => r["application_name"] == "{application}")
    |> filter(fn: (r) => r["f_port"] == "1")
    |> aggregateWindow(every: {period}, fn: last, createEmpty: false)
    |> yield(name: "last")"""
    
    return query_string

class InfluxDbHelper:
    
    __instance = None

    @staticmethod
    def get_instance():
        if InfluxDbHelper.__instance == None:
            InfluxDbHelper.__instance = InfluxDbHelper()
        return InfluxDbHelper.__instance
    
    def __init__(self) -> None:
        self._token =  config('INFLUXDB_TOKEN')
        self._org =  config('INFLUXDB_ORG')
        self._bucket =  config('INFLUXDB_BUCKET')
        self._url =  config('INFLUXDB_URL')
        
    def _do_query(self, query):
        time_stamp = []
        values = []
        with InfluxDBClient(url= self._url, token=self._token, org=self._org) as client:
            tables = client.query_api().query(query, org=self._org)
            for table in tables:
                for record in table.records:
                    date = record.get_time()
                    date += timedelta(hours = 8)
                    time_stamp.append(date.strftime("%Y-%m-%d %H:%M:%S"))
                    values.append(round(record.get_value(),3))
                    
                    
        return time_stamp, values           
        
        
    def _do_query_parameter(self, query) -> typing.List[str]:
        result = []
        try: 
            with InfluxDBClient(url= self._url, token=self._token, org=self._org) as client:
                tables = client.query_api().query(query, org=self._org)
                for table in tables:
                    for record in table:
                        app_name = record.get_value()
                        result.append(app_name)
        except Exception as e:
            logging.exception(f"Query InfluxDB has errors. {str(e)}")
            return []   
        return result
         
    @cached(cache=TTLCache(maxsize=1024, ttl=60))
    def get_history_data(self, measurement, dev_eui, application, period='30m', time_range="72h"):
        query = get_history_data_query_string(bucket=self._bucket, 
                                      time_range=time_range, measurement= measurement, 
                                      application=application, period= period, dev_eui= dev_eui)
        return self._do_query(query=query)
    
    
    def get_all_measurements(self, measurement_prefix = "device_frmpayload_data_" ):
        query = f"""
                import \"influxdata/influxdb/schema\"
                schema.measurements(bucket: \"{self._bucket}\")
                """
        all_measurements = self._do_query_parameter(query)
        result = [measurement for measurement in all_measurements if measurement.startswith(measurement_prefix)]
        return result
            
    
    def get_all_device_ids(self, since = "-1w", 
                                  on_measurement = "device_frmpayload_data_battery" ) -> typing.List[str]:
        query = f"""from(bucket: "{self._bucket}")
                |> range (start: {since})
                |> filter(fn:(r) => r._measurement == "{on_measurement}")
                |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
                |> group()
                |> distinct(column: "dev_eui")"""

        return self._do_query_parameter(query)
                    
    
    def get_all_application_names(self, since = "-1w", 
                                  on_measurement = "device_frmpayload_data_battery" ) -> typing.List[str]:
        query = f"""from(bucket: "{self._bucket}")
                |> range (start: {since})
                |> filter(fn:(r) => r._measurement == "{on_measurement}")
                |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
                |> group()
                |> distinct(column: "application_name")"""
        
        return self._do_query_parameter(query)

    
if __name__ == "__main__":
    influxdb_helper = InfluxDbHelper.get_instance()
    result = influxdb_helper.get_all_measurements() 
    print(result)
    