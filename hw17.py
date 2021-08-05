#!/usr/bin/python3
# https://coderoad.ru/44636152/%D0%9A%D0%B0%D0%BA-%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5-EXIF-%D0%B2-python
# https://habr.com/ru/company/mailru/blog/512004/

import subprocess
from GPSPhoto import gpsphoto


def write_coord(file, latitude, longitute):
    photo = gpsphoto.GPSPhoto(file)
    # Create GPSInfo Data Object
    info = gpsphoto.GPSInfo((latitude, longitute))
    # Modify GPS Data
    photo.modGPSData(info, file)


def get_coord(file):
    all_info_dict = gpsphoto.GPSPhoto(file).gpsData
    return f"{all_info_dict['Latitude']}';{all_info_dict['Longitude']}'"


# write_coord('hw17.jpg', 29.9789891, 31.1337324)
coord = get_coord('hw17.jpg').replace('\'', '').replace(';', ',')
res = subprocess.Popen(['python3', 'hw16.py', coord], stdout=subprocess.PIPE)
print(res.stdout.read().decode())





