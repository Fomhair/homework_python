import csv


def parse_csv(path):
    with open(path, 'r') as data:
        data = list(csv.reader(data))
        return data
