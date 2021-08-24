#!/usr/bin/python3

# Написать класс router.
# Должен иметь методы добавить/удалить/вывести список ip address.
# Должен иметь методы добавить/удалить/вывести список ip routes.
#
# Есть маршруты к непосредственно-подключенным сетям:
# если у устройства есть ip-address 192.168.5.14/24 на интерфейсе eth1,
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
# https://docs.python.org/3/library/ipaddress.html
# https://pythonworld.ru/osnovy/formatirovanie-strok-metod-format.html

import ipaddress


class Router:
    """
    router is a class that stores information about routes and ip addresses
    """
    def __init__(self):
        self.routes_table = []

    def visual_decorator(func_to_decorate):
        def wrap_func(self):
            print('-' * 125)
            print("|{:^30}|{:^30}|{:^30}|{:^30}|".format("Маска подсети", "IP-адрес подсети", "Интерфейс", "Шлюз"))
            print('-' * 125)
            func_to_decorate(self)
            print('-' * 125)
        return wrap_func

    def add_datas(self, ip, interface):
        """ Create a dictionary with data and add in routes_table """
        res_dict = {}
        try:
            res_dict['gateway'] = ipaddress.IPv4Interface(ip).ip
            res_dict['netmask'] = ipaddress.IPv4Interface(ip).netmask
            res_dict['network_ip'] = str(ipaddress.ip_network(ip, False).network_address) # ipaddress.IPv4Interface(ip).network
            res_dict['interface'] = interface
            self.routes_table.append(res_dict)
        except:
            print('exception')

    def add_ip_address(self, ip_address_mask, iface_name):
        """
        add ip-address in routes_table
        """
        self.add_datas(ip_address_mask, iface_name)

    def del_ip_address(self, ip_address_mask, iface_name):
        """
        Func removes ip-address with given iface
        """
        for el in self.routes_table:
            if el['gateway'] == ipaddress.IPv4Interface(ip_address_mask).ip and el['interface'] == iface_name:
                self.routes_table.remove(el)

    @visual_decorator
    def show_ip_address(self):
        """
        :return: show all ip-addresses in class
        """
        for el in self.routes_table:
            try:
                ipaddress.IPv4Address(el['interface'])
            except ipaddress.AddressValueError:
                print("|{:^30}|{:^30}|{:^30}|{:^30}|".format(str(el['netmask']), str(el['network_ip']), str(el['interface']), str(el['gateway'])))
                #    f"Маска подсети: {el['netmask']} IP-адрес подсети: {el['network_ip']},"
                #      f" Интерфейс: {el['interface']}, Шлюз: {el['gateway']}")

    def add_ip_routes(self, ip_address_mask, gateway):
        """
        check and add new route
        """

        flag = False
        for route in self.routes_table:
            dest_network_ip, mask = route["network_ip"], route["netmask"]
            current_gw_network_ip = str(ipaddress.ip_network(f"{gateway}/{mask}", False).network_address)
            if dest_network_ip == current_gw_network_ip:
                self.add_datas(ip_address_mask, gateway)
                print(f'ok - добавлен маршрут до {ip_address_mask} через {gateway}')
                flag = True

        if not flag:
            print(f'excepton - маршрут до {ip_address_mask} через {gateway} не может быть добавлен')

    def del_ip_routes(self, ip_address_mask, iface):
        """
        delete routes
        """
        for el in self.routes_table:
            if el['gateway'] == ipaddress.IPv4Interface(ip_address_mask).ip and \
                    el['netmask'] == ipaddress.IPv4Interface(ip_address_mask).netmask and el['interface'] == iface:
                self.routes_table.remove(el)

    @visual_decorator
    def show_ip_routes(self):
        """
        print all routes from routes_table
        """
        for el in self.routes_table:
            # print(el)
            try:
                ipaddress.IPv4Address(el['interface'])
                print("|{:^30}|{:^30}|{:^30}|{:^30}|".format(str(el['netmask']),
                        str(el['network_ip']), str(el['interface']), str(el['gateway'])))
                # print(f"Маска подсети: {el['netmask']} IP-адрес подсети: {el['network_ip']},"
                #      f" Интерфейс: {el['interface']}, IP-адрес: {el['gateway']}")
            except ipaddress.AddressValueError:
                pass


# test
new_rout = Router()
new_rout.add_ip_address('192.168.5.14/24', 'eht1')
print(new_rout.routes_table)
new_rout.del_ip_address('192.168.5.14/24', 'eht1')
print(new_rout.routes_table)
new_rout.add_ip_address('192.168.5.14/24', 'eht1')
new_rout.add_ip_address("192.168.15.55/27", "eth1")
new_rout.add_ip_address("192.185.3.11/28", "eth2")
new_rout.show_ip_address()
new_rout.add_ip_routes("172.16.0.0/16", "192.168.5.1")
new_rout.add_ip_routes("172.24.0.0/16", "192.168.8.1")
new_rout.add_ip_routes("172.24.0.0/16", "172.16.8.1")
new_rout.show_ip_routes()
for el in new_rout.routes_table:
    print(el)
new_rout.show_ip_address()
print('-')
new_rout.show_ip_routes()
new_rout.del_ip_routes('172.16.0.0/16', '192.168.5.1')
new_rout.show_ip_routes()

# Добавляем ip-address 192.168.5.14/24 eth1.
# Добавляем маршрут до 172.16.0.0/16 через 192.168.5.1 - ok.
# Добавляем маршрут до 172.24.0.0/16 через 192.168.8.1 - exception.
# Добавляем маршрут до 172.24.0.0/16 через 172.16.8.1 - ok.