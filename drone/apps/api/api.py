from rest_framework.response import Response
from rest_framework import viewsets, generics, filters
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from ..models import *
from .serializers import *


class DroneViewSet(viewsets.ModelViewSet):
    """
    API View for Drone serializer, using crud methods.
    GET: for get all instance of the Drone model in data base.
    POST: for create instances of the Drone model in data base.
    PUT: for update instances of the Drone model in data base.
    DELETE: for delete instance of the Drone model in data base.
    """
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    """
    API View for Medication serializer, using crud methods.
    GET: for get all instance of the Medication model in data base.
    POST: for create instances of the Medication model in data base.
    PUT: for update instances of the Medication model in data base.
    DELETE: for delete instance of the Medication model in data base.
    """
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class LoadedMedicationForDrone(generics.ListAPIView):
    """
    API for check loaded medication items for a given drone.
    Input: drone pk
    """
    serializer_class = MedicationSerializer
    queryset = Medication.objects.all()


class DroneBatteryLevel(generics.RetrieveAPIView):
    """
    API for check drone battery level for a given drone.
    Input: drone pk
    """
    serializer_class = BatteryDroneSerializer
    queryset = Drone.objects.all()

