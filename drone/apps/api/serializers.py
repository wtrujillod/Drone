from rest_framework import serializers
from.service import *


class DroneSerializer(serializers.ModelSerializer):
    """
    Serializer for instances of the Drone model. Contains all the fields of the model.
    """

    class Meta:
        model = Drone
        fields = '__all__'

    def create(self, validated_data):
        drone = Drone.objects.create(**validated_data)
        complete_data_extension(drone.pk, drone.model)
        return drone


class BatteryDroneSerializer(serializers.ModelSerializer):
    """
    Serializer for instances of the Drone model. Contains pk, serial_number and battery_level fields of the model.
    """

    class Meta:
        model = Drone
        fields = ['pk', 'serial_number', 'battery_level']

    def to_representation(self, instance):
        return {
            'id': instance.pk,
            'serial_number': instance.serial_number,
            'battery_level': instance.battery_level
        }


class StateDroneSerializer(serializers.ModelSerializer):
    """
    Serializer for instances of the Drone model. Contains pk, serial_number, battery_level and state fields of the model.
    """

    class Meta:
        model = Drone
        fields = ['pk', 'serial_number', 'battery_level', 'state']

    def to_representation(self, instance):
        return {
            'id': instance.pk,
            'serial_number': instance.serial_number,
            'battery_level': instance.battery_level,
            'state': instance.state
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
    Serializer for add instance of the Drone model in instance of the Medication model.
    Contains pk, name, weight and drone the fields of the models.
    """
    class Meta:
        model = Medication
        fields = ['id', 'name', 'weight', 'drone']
