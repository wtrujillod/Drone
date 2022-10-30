from ..models import *


def change_battery_level(pk):
    drone = Drone.objects.filter(id=pk).first()
    print(drone.battery_level)
