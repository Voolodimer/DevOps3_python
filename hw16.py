#!/usr/bin/python3
import sys
from geopy.geocoders import Nominatim


def get_place(file, coordinates):
    geolocator = Nominatim(user_agent="hw16")
    if file:
        coord = ''
        with open('coordinates.txt') as file:
            # считываем координаты, разбиваем по ;, меняем , на .
            coord = [','.join(el.rstrip('\n').replace(',', '.').replace('\'', '').split(';')) for el in file.readlines()]

    if coordinates:
        coord = []
        coord.append(coordinates)

    for el in coord:
        try:
            location = geolocator.reverse(el)
            print('Location:', location.address)
            print('Goggle Maps URL:', f'https://www.google.com/maps/search/?api=1&query={el}')
        except:
            print('error')


if len(sys.argv) == 2:
    get_place(0, sys.argv[1])
else:
    get_place('coordinates.txt', 0)





