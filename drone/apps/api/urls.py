from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .api import *

urlpatterns = [
    path('api/', include('apps.api.routers')),
    path('medications_for_drone/<int:drone>/', LoadedMedicationForDrone.as_view(), name='LoadedMedicationForDrone'),
    path('drone_battery_level/<int:pk>/', DroneBatteryLevel.as_view(), name='DroneBatteryLevel'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
