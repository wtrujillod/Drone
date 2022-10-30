from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .api import *

urlpatterns = [
    path('crud/', include('apps.api.routers')),
    path('medications_for_drone/<int:drone>/', LoadedMedicationForDrone.as_view(), name='LoadedMedicationForDrone'),
    path('drone_battery_level/<int:pk>/', DroneBatteryLevel.as_view(), name='DroneBatteryLevel'),
    path('available_drone_for_loading/', AvailableDroneForLoading.as_view(), name='AvailableDroneForLoading'),
    path('loading_medications_drone/<int:pk>/', LoadingDroneWithMedication.as_view(), name='LoadingDroneWithMedication'),
    path('change_state_drone/<int:pk>/', ChangeStateDrone.as_view(), name='ChangeStateDrone'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
