from jinja2 import Environment, FileSystemLoader
from pprint import pprint
import csv

SOURCE = 'sources/707n.csv'

def get_data():
    with open(SOURCE) as csvfile:
        reader= csv.reader(csvfile, delimiter=';')
        data = []
        for row in reader:
            item = {'ord': '', 'dest': []}
            item['ord'] = row[0]
            item['dest'] = [i for i in row[1:] if i]
            item['dest'] = sorted(item['dest'])
            data.append(item)
    return data



if __name__ == '__main__':
    pprint(get_data())