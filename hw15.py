#!/usr/bin/python3

# Написать класс router.
# Должен иметь методы добавить/удалить/вывести список ip address.
# Должен иметь методы добавить/удалить/вывести список ip routes.
#
# Есть маршруты к непосредственно-подключенным сетям:
# если у устройства есть ip-adress 192.168.5.14/24 на интерфейсе eth1,
# значит у него должен быть маршрут:
# к сети 192.168.5.0/24 через eth1 или через 192.168.5.14.
#
# Если мы хотим добавить маршрут к какой-нибудь удаленной сети,
# то надо проверять доступен ли gateway.
#
# Например мы можем добавить маршрут к 172.16.0.0/16 через gateway
# 192.168.5.132, только если у нас уже есть маршрут до 192.168.5.132.
#
# Если же мы попытаемся добавить маршрут до какой-либо сети через gateway,
# до которого у нас пока еще нет маршрута, то должен вылетать exception.
#
# Например:
# Добавляем ip-address 192.168.5.14/24 eth1.
# Добавляем маршрут до 172.16.0.0/16 через 192.168.5.1 - ok.
# Добавляем маршрут до 172.24.0.0/16 через 192.168.8.1 - exception.
# Добавляем маршрут до 172.24.0.0/16 через 172.16.8.1 - ok.
#
# Итого - 1 интерфейс и 3 маршрута в таблице.

import os
import netifaces
import subprocess


class Router:
    '''

    '''
    def add_ip_address(self, iface_name, ip_address, netmask):
        iface_name, ip_address, netmask = map(str, (iface_name, ip_address, netmask))
        return os.system(f"sudo -S ifconfig {iface_name} {ip_address} netmask {netmask}")

    def del_ip_address(self, iface_name):
        return os.system(f"sudo -S ifconfig {iface_name} 0.0.0.0")
        # ip addr del 192.168.0.77/24 dev eth0

    def show_ip_address(self):
        for iface in netifaces.interfaces():
            iface_details = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in iface_details:
                print(iface_details[netifaces.AF_INET])
                # print(iface_details[netifaces.AF_INET][0]['addr'])

    def add_ip_routes(self, ip_addr_mask, gateway, host_or_net):
        try:
            subprocess.call(f"sudo -S route add -{host_or_net} {ip_addr_mask} gw {gateway}", shell=True)
            print('ok')
            # os.system(f"sudo -S route add -net {ip_addr_mask} gw {gateway}")
        except Exception as e:
            print('exception', e)
        # route add -net 10.10.0.0/16 gw 10.10.1.1
        # ip route add 10.10.0.0/16 via 10.10.1.1

    def del_ip_routes(self, ip_address, gateway, host_or_net):
        return subprocess.call(f"sudo -S route delete -{host_or_net} {ip_address} gw {gateway}", shell=True)
        # route delete -net 10.10.0.0 netmask 255.255.0.0

    def show_ip_routes(self):
        return subprocess.call("ip route", shell=True)


# Router.show_ip_routes(Router)
# Router.add_ip_address(Router, 'enp4s0', '192.168.0.125', '255.255.255.0')
# Router.del_ip_address(Router, 'enp4s0')
# Router.show_ip_address(Router)
# Router.show_ip_routes(Router)
# Router.add_ip_routes(Router, '10.32.234.1', '192.168.0.1', 'host')
# Router.del_ip_routes(Router, '10.32.234.1', '192.168.0.1', 'host')
# Router.show_ip_routes(Router)
