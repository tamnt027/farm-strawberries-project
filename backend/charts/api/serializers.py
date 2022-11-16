
from rest_framework import serializers
from charts.influxdb_helper import InfluxDbHelper
from charts.models import Chart, ChartGroup, SeriesDisplay

class ChartGroupListSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source='name')
    # description = serializers.CharField('')
    class Meta:
        model = ChartGroup
        fields = [
            'id',
            'name',
            'description',

        ]
        
        
class SeriesDisplayDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesDisplay
        fields = [
            'id',
            'name',
            'mode',
            'chart_type',
            'color',
            'yaxis',
        ]
    pass        

class ChartSerializer(serializers.ModelSerializer):
    group = ChartGroupListSerializer()
    class Meta:
        model = Chart
        fields = ['id', 'name', 'title', 'group', 'data',
            'frames',
            'layout',
            'config',]
        
    data = serializers.SerializerMethodField('get_data')
    frames = serializers.SerializerMethodField('get_frames')
    layout = serializers.SerializerMethodField('get_layout')
    config = serializers.SerializerMethodField('get_config')
    

    
    def get_data(self, chart : Chart ):
        return []
    
    def get_frames(self, chart):
        return []
    
    def get_layout(self, chart: Chart):
        return {}
    
    def get_config(self, chart):
        return {}
        
class ChartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = [
            'id',
            'name',
            'data',
            'frames',
            'layout',
            'config',
        ]
        
    data = serializers.SerializerMethodField('get_data')
    frames = serializers.SerializerMethodField('get_frames')
    layout = serializers.SerializerMethodField('get_layout')
    config = serializers.SerializerMethodField('get_config')
    # // const [state, setState] = useState({
    # //     data: [{
    # //         x: [1, 2, 3],
    # //         y: [2, 6, 3],
    # //         type: 'scatter',
    # //         mode: 'lines+markers',
    # //         marker: {color: 'red'},
    # //       }],
    # //     layout: {},
    # //     frames:[],
    # //     config: {}
    # // })
    
    def get_data(self, chart : Chart ):
        results = []
        influxdb_helper = InfluxDbHelper.get_instance()
        series_display : SeriesDisplay   # type annotation purpose only
        annotations_array = []
        offset = 0
        for series_display in chart.series_displays.all():
            (timestamps, values) = influxdb_helper.get_history_data(series_display.measurement.name,
                                                                series_display.device.device_id, chart.group.name)
            # results.append({
            #     "x": timestamps,
            #     "y": values,
            #     "type": series_display.chart_type,
            #     "mode": series_display.mode,
            #     "marker": {"color": series_display.color}
            # })
            
            data = {"type" : series_display.chart_type,
                    "mode" : series_display.mode,
                    "name" : series_display.name,
                    "yaxis": series_display.yaxis,
                    "line": {
                                "color": series_display.color,
                                "width": 2,
                            },
                    "x": timestamps,
                    "y": values}
            
            results.append(data)
        return results
            
        
    def get_frames(self, chart):
        return []
    
    def get_layout(self, chart: Chart):
        annotations_array = []
        offset = 0
        for series_display in chart.series_displays.all():
            influxdb_helper = InfluxDbHelper.get_instance()
            (timestamps, values) = influxdb_helper.get_history_data(series_display.measurement.name,
                                                                series_display.device.device_id, chart.group.name)
            annotation = {
                        "xref": 'paper',
                        "yref" : 'paper',
                        "x": 1.1,
                        "y": 1 - offset,
                        "xanchor": 'left',
                        "yanchor": 'middle',
                        "text": str(round(values[-1],1)),
                        "font": {
                            "family": 'Arial',
                            "size": 20,
                            
                            "color": series_display.color
                        },
                        "showarrow": False
                        }
            annotations_array.append(annotation)
            
            offset += 0.1
        
        layout = {
            "title": {
                "text": chart.title,
                "font": {
                        "family": 'Arial',
                        "size": chart.title_size,
                        "color": chart.title_color
                    }
            },
            "autosize": True,
            "xaxis": {
                "type": 'date'
            },
            "yaxis": {
                "autorange": True,
                "zeroline": False,
                "type": 'linear',
            },
            "yaxis2": {
                "autorange": True,
                "zeroline": False,
                "overlaying": "y",
                "side": "right"
            },
            "yaxis3": {
                "autorange": True,
                "zeroline": False,
                "overlaying": "y",
                "side": "left",
                "anchor" :"free",
                "tickfont" : {
                    "color": "red",
                    "position" : 2,
                }
            },
            "yaxis4": {
                "autorange": True,
                "zeroline": False,
                "overlaying": "y",
                "side": "right",
                "tickfont" : {
                    "color": "red",
                    "position" : 2,
                }
            },
            "legend": {"orientation": 'h', 
                       "side": 'top'},
            # "paper_bgcolor":"LightSteelBlue",
            "margin" : dict(l=50, r=110, t=50, b=0),
            "annotations" : annotations_array,
        } 
        
        return layout
    
    def get_config(self, chart):
        return {}
    
class ChartGroupDetailSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source='name')
    # description = serializers.CharField('')
    charts = ChartSerializer(many=True)
    class Meta:
        model = ChartGroup
        fields = [
            'id',
            'name',
            'description',
            'charts',

        ]