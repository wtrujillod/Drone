from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .api import *

urlpatterns = [
    path('drones/', DroneAPIView.as_view(), name="drone_api"),
    path('medication/', MedicationAPIView.as_view(), name="medication_api"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
