from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from simple_history.models import HistoricalRecords

WEIGHT_LIST = [
    ('LW', 'Lightweight'),
    ('MW', 'Middleweight'),
    ('CW', 'Cruiserweight'),
    ('HW', 'Heavyweight')
]

WEIGHT_DATA_EXT = {
    'LW': [900, 2],
    'MW': [1200, 5],
    'CW': [3000, 8],
    'HW': [6200, 10]
}

STATE_LIST = [
    (1, 'IDLE'),
    (2, 'LOADING'),
    (3, 'LOADED'),
    (4, 'DELIVERING'),
    (5, 'DELIVERED'),
    (6, 'RETURNING')
]


# Create your models here.
class Drone(models.Model):
    serial_number = models.CharField(max_length=100, blank=False, null=False)
    model = models.CharField(max_length=15, choices=WEIGHT_LIST)
    weight_limit = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    battery_capacity = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(100)])
    battery_level = models.IntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)])
    state = models.IntegerField(choices=STATE_LIST)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = "Drone"
        verbose_name_plural = "Drones"

    def __str__(self):
        return f'{self.serial_number}'

    def change_batt_lv(self, level):
        self.battery_level = level
        self.save()
        return True


class Medication(models.Model):
    name = models.CharField(max_length=250,
                            validators=[RegexValidator(regex=r"^[a-zA-Z0-9\-\_]+$", message="Invalid Field")])
    weight = models.IntegerField()
    code = models.CharField(max_length=250,
                            validators=[RegexValidator(regex=r"^[A-Z0-9\_]+$", message="Invalid Field")])
    image = models.ImageField(null=True, blank=True, upload_to="medication/%Y%m%d")
    drone = models.ForeignKey(Drone, related_name="medicts_drone", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Medication"
        verbose_name_plural = "Medications"

    def __str__(self):
        return f'{self.name} {self.code}'


class DataExtension(models.Model):
    table_extension = models.CharField(max_length=100)
    field_extension = models.CharField(max_length=255)
    key_register = models.IntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Data Extension"
        verbose_name_plural = "Data Extensions"

    def __str__(self):
        return f'{self.field_extension} {self.value}'
