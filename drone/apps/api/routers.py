from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from .api import *

router = DefaultRouter()

router.register(r'drones_crud', DroneViewSet)
router.register(r'medications_crud', MedicationViewSet)

urlpatterns = router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
