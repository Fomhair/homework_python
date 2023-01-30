import generator.scooters as g
import os
import configparser
import parse_data as p
import view.methods as view
from random import randint


def init_new_datafile(name, data_src, size, creation_method):
    config = configparser.ConfigParser()
    config.read('config.ini')
    data_dir = config['DEFAULT']['data_dir']
    data_file = name+config['DEFAULT']['data_file_ext']
    data_path = os.path.join(data_dir, data_file)

    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    if not os.path.exists(data_path):
        data_src(creation_method, data_path, size)

    return data_path


def init(name, f, size):
    result = init_new_datafile(name, g.create_file, size, f)
    return p.parse_csv(result)


def show_random_scooter():
    scooters = init('scooters', g.generate_scooters_list, 300)
    sc_header = scooters[0]
    scooters_list = scooters[randint(1, 299)]

    view.entry(view.html, scooters_list, sc_header)
    view.entry(view.console, scooters_list, sc_header)

    print('______')
    hubs = init('hubs', g.generate_hubs_list, 4)
    hubs_header = hubs[0]
    hubs_list = hubs[randint(1, 4)]

    view.entry(view.html, hubs_list, hubs_header)
    view.entry(view.console, hubs_list, hubs_header)

    return scooters_list, hubs_list
