from random import randint as rnd, random
from datetime import datetime as dt


def generate_scooter(scooter_id, hubs=4):
    scooter = {
        'scooter_id': scooter_id,
        'hub_id': rnd(1, hubs),
        'service_id': 0,
        'status': 1,
        'status_update': dt(2022, 5, 10, 12, 0, 0),
        'location_x': round(random() * 500 - 250, 3),
        'location_y': round(random() * 500 - 250, 3),
        'charge': 1.00
    }
    return scooter


def generate_scooters_list(size):
    scooters = [generate_scooter(i) for i in range(size)]
    return scooters


def generate_hub(hub_id):
    hub = {
        'hub_id': hub_id,
        'service_id': 0,
        'hub_status': 1,
        'status_update': dt(2022, 5, 10, 12, 0, 0),
    }
    return hub


def generate_hubs_list(size):
    scooters = [generate_hub(i) for i in range(size)]
    return scooters


def create_line(items, mod=True):
    line = ''
    for item in items:
        if mod:
            line += f'{item},'
        else:
            line += f'{items[item]},'
    return line[:len(line) - 1] + '\n'


def create_file(set_generator, path, size):
    with open(path, "w") as data:
        items = set_generator(size)
        data.write(create_line(items[0]))
        for item in items:
            data.write(create_line(item, False))

