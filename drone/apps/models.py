from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from simple_history.models import HistoricalRecords

WEIGHT_LIST = [
    ('LW', 'Lightweight'),
    ('MW', 'Middleweight'),
    ('CW', 'Cruiserweight'),
    ('HW', 'Heavyweight')
]

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
    battery_capacity = models.IntegerField()
    state = models.IntegerField(choices=STATE_LIST)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = "Drone"
        verbose_name_plural = "Drones"

    def __str__(self):
        return f'{self.serial_number}'


class Medication(models.Model):
    name = models.CharField(max_length=250, validators=[RegexValidator(regex=r"^[a-zA-Z0-9\-\_]+$", message="Invalid Field")])
    weight = models.IntegerField()
    code = models.CharField(max_length=250, validators=[RegexValidator(regex=r"^[A-Z0-9\_]+$", message="Invalid Field")])
    image = models.ImageField(null=True, blank=True, upload_to="medication/%Y%m%d")
    drone = models.ForeignKey(Drone, related_name="medicts_drone", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Medication"
        verbose_name_plural = "Medications"

    def __str__(self):
        return f'{self.name} {self.code}'
