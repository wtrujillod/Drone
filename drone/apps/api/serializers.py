from rest_framework import serializers
from ..models import *


class DroneSerializer(serializers.ModelSerializer):
    """
    Serializer for instances of the Drone model. Contains all the fields of the model.
    """

    class Meta:
        model = Drone
        fields = '__all__'


class BatteryDroneSerializer(serializers.ModelSerializer):
    """
    Serializer for instances of the Drone model. Contains pk, serial_number, battery_capacity fields of the model.
    """

    class Meta:
        model = Drone
        fields = ['pk', 'serial_number', 'battery_capacity']

    def to_representation(self, instance):
        return {
            'id': instance.pk,
            'serial_number': instance.serial_number,
            'battery_capacity': instance.battery_capacity
        }


class MedicationSerializer(serializers.ModelSerializer):
    """
    Serializer for instances of the Medication model. Contains all the fields of the model.
    """
    drone = serializers.StringRelatedField()

    class Meta:
        model = Medication
        fields = '__all__'


class DroneWithMedicationSerializer(serializers.ModelSerializer):
    """
    Serializer for add instance of the Drone model in instance of the Medication model. Contains all the fields of the models.
    """
    class Meta:
        model = Medication
        fields = ['id', 'name', 'weight', 'drone']
