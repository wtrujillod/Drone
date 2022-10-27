from rest_framework import serializers
from ..models import *


class DroneSerializer(serializers.ModelSerializer):
    """
    Serializer for instances of the Drone model. Contains all the fields of the model.
    """
    class Meta:
        model = Drone
        fields = '__all__'


class MedicationSerializer(serializers.ModelSerializer):
    """
    Serializer for instances of the Medication model. Contains all the fields of the model.
    """
    class Meta:
        model = Medication
        fields = '__all__'
