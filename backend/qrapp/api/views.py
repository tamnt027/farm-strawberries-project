from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics

from qrapp.models import QRCode, BarCode 

from .serializers import (BarCodeListSerializer,
                          BarCodeCreateSerializer,
)


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)


class BarCodeListAPIView(generics.ListAPIView):
    queryset = BarCode.objects.all()
    serializer_class = BarCodeListSerializer
    permission_classes = [AllowAny]
    
    
class BarCodeCreateAPIView(generics.CreateAPIView):
    serializer_class = BarCodeCreateSerializer
    queryset = BarCode.objects.all()
    permission_classes = [AllowAny]
    # throttle_scope = 'create_barcode'