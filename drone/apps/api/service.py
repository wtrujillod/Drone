from simple_history.utils import update_change_reason

from ..models import *


def complete_data_extension(pk, model):
    table_extension = 'DRONE'
    field_extension = ['mah_capacity', 'min_battery']
    value = [WEIGHT_DATA_EXT[model][0], WEIGHT_DATA_EXT[model][1]]

    for i in range(len(field_extension)):
        DataExtension(table_extension=table_extension,
                      field_extension=field_extension[i],
                      key_register=pk,
                      value=value[i]).save()


def change_battery_level(pk):
    drone = Drone.objects.filter(id=pk).first()
    data_extension = dict(DataExtension.objects.filter(table_extension='DRONE', key_register=pk).values_list(
        'field_extension', 'value'))

    med_drone = list(Medication.objects.filter(drone=drone).values_list('weight'))
    weight = sum([med_drone[i][0] for i in range(len(med_drone))])

    battery_capacity = drone.battery_capacity
    battery_level = drone.battery_level
    mah_capacity = int(data_extension['mah_capacity'])
    minimum_battery = int(data_extension['min_battery'])

    load_weight = round((weight / drone.weight_limit) * 100, 2)
    real_battery_capacity = round((battery_capacity / 100) * mah_capacity, 2)
    available_battery_capacity = round(((battery_level - minimum_battery) / 100) * real_battery_capacity, 2)
    battery_consumption = round((load_weight / 100) * available_battery_capacity, 2)
    percentage_battery_consumption = round((battery_consumption / real_battery_capacity) * 100, 2)

    battery_level = round(battery_level - percentage_battery_consumption)
    drone.battery_level = battery_level
    drone.save()
    update_change_reason(drone, 'Change battery level')

    medications_drone = Medication.objects.filter(drone=drone)
    for medication in medications_drone:
        medication.drone = None
        medication.save()
