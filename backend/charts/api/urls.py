from django.urls import include, path
from django.contrib import admin

from .views import (
    ChartGroupListAPIView,
    ChartGroupDetailAPIView,
    # UserLoginAPIView,
    # UserLogoutAPIView,
    # UserDetailAPIView,
    # UserListAPIView,
    # UserDeleteAPIView,
    # UserUpdateAPIView
    import_chart_group,
    import_devices,
    import_measurements,
)

urlpatterns = [
    path('import/chart_group/', import_chart_group, name='import-chart-group'  ),
    path('import/device/', import_devices, name='import-device'  ),
    path('import/measurement/', import_measurements, name='import-measurement'  ),
    
    path('group/', ChartGroupListAPIView.as_view(), name='chart-group-list'),
    path('group/<slug:pk>/', ChartGroupDetailAPIView.as_view(), name='chart-group-detail'),
    # path('register/', UserCreateAPIView.as_view(), name='user-register'),
    # path('login/', UserLoginAPIView.as_view(), name='user-login'),
    # path('logout/', UserLogoutAPIView.as_view(), name='user-logout'),
    # path('<slug:username>/', UserDetailAPIView.as_view(), name='user-detail'),
    # path('<slug:username>/edit/', UserUpdateAPIView.as_view(), name='user-update'),
    # path('<slug:username>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),
]
