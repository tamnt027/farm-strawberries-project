from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from charts.models import Chart, LoraMeasurement, ChartGroup
from .serializers import ChartGroupDetailSerializer, ChartGroupListSerializer
from charts import utility
from django.conf import settings

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)


class ChartGroupListAPIView(generics.ListAPIView):
    queryset = ChartGroup.objects.all()
    serializer_class = ChartGroupListSerializer
    permission_classes = [AllowAny]
    
class ChartGroupDetailAPIView(generics.RetrieveAPIView):
    queryset = ChartGroup.objects.all()
    serializer_class = ChartGroupDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]


@csrf_exempt
@require_http_methods(["POST"])
def import_chart_group(request):
    try:
        #TODO : Only admin can do this
        utility.import_chart_group_from_influxdb()
    except:
        return HttpResponse({"status": "failed"})
    return JsonResponse({"status": "success"})


@csrf_exempt
@require_http_methods(["POST"])
def import_measurements(request):
    try:
        #TODO : Only admin can do this
        utility.import_measurements_from_influxdb()
    except:
        return HttpResponse({"status": "failed"})
    return JsonResponse({"status": "success"})

@csrf_exempt
@require_http_methods(["POST"])
def import_devices(request):
    try:
        #TODO : Only admin can do this
        utility.import_devices_from_influxdb()
    except:
        return HttpResponse({"status": "failed"})
    return JsonResponse({"status": "success"})



# class LoraApplicationViewSet(viewsets.ViewSet):
    
#     def list(self, request):
#         queryset = LoraApplication.objects.all()
#         serializer = LoraApplicationSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk=None):
#         queryset = LoraApplication.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = LoraApplicationSerializer(user)
#         return Response(serializer.data)
#     pass

# class ChartViewSet(viewsets.ModelViewSet):
#     queryset = Chart.objects.all() 
#     serializer_class = ChartSerializer
#     # permission_classes =  [permissions.IsAuthenticatedOrReadOnly]
    
#     def get_permissions(self):
#         # if self.action == "list":
#         #     return [permissions.IsAuthenticatedOrReadOnly]
#         return super().get_permissions()
    
    
#     # @action(methods=['post'], detail=True, url_path="hide-lesson", url_name="hide-lesson")
#     # def hide_lesson(self, request, pk):
#     #     try:
#     #         pass
#     #     except Chart.DoesNotExist():
#     #         return Response(status=status.HTTP_400_BAD_REQUEST)
#     #     return Response(data=LessonSerializer(l, context={'request': request}), status=status.HTTP_200_OK)
    
# class LoraMeasurementViewSet(viewsets.ViewSet, generics.ListAPIView):
#     queryset = LoraMeasurement.objects.all()
#     serializer_class = LoraMeasurementNameSerializer
    
    