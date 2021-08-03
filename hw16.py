#!/usr/bin/python3

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="hw16")
coord = ''
with open('coordinates.txt') as file:
    # считываем координаты, разбиваем по ;, меняем , на .
    coord = [','.join(el.rstrip('\n').replace(',', '.').replace('\'', '').split(';')) for el in file.readlines()]


for el in coord:
    try:
        location = geolocator.reverse(el)
        print('Location:', location.address)
        print('Goggle Maps URL:', f'https://www.google.com/maps/search/?api=1&query={el}')
    except:
        print('error')
