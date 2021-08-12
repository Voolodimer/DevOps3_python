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

import ipaddress


class Router:
    """
    router is a test class
    """

    def __init__(self):
        self.route_table = []

    def add_ip_address(self, iface_name, ip_address, netmask):
        """
        :param iface_name: - interface name
        :param ip_address:
        :param netmask:
        :return: 1 or 0
        """
        return 1

    def del_ip_address(self, iface_name):
        '''
        :param iface_name:
        :return:
        '''
        return 1
        # ip addr del 192.168.0.77/24 dev eth0

    def show_ip_address(self):
        """
        :return: all ip-addresses in class
        """

    def add_ip_routes(self, ip_addr_mask, gateway, host_or_net):
        """
        :param ip_addr_mask:
        :param gateway: 
        :param host_or_net:
        :return:
        """
        return 1
        # route add -net 10.10.0.0/16 gw 10.10.1.1
        # ip route add 10.10.0.0/16 via 10.10.1.1

    def del_ip_routes(self, ip_address, gateway, host_or_net):
        """
        :param ip_address:
        :param gateway:
        :param host_or_net:
        :return:
        """
        return 1
        # route delete -net 10.10.0.0 netmask 255.255.0.0

    def show_ip_routes(self):
        """
        :return:
        """
        return 1


