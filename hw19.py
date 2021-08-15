#!/usr/bin/python3

# Написать dns сервер.
# Сервер должен принимать соединения по протоколу udp.
# Если приходит запрос "domain.name" должен отправлять в ответ ip адрес.
# * Доп задание: иметь возможность переопределять записи клиентами:
# * ADD my.google.com:228.228.228.228

import socket as sock


def check_str_type(host):
    i = len(host.decode()) - 1
    host_str = host.decode()
    is_str = False
    while i >= 0:
        if 48 <= ord(host_str[i]) <= 57 or ord(host_str[i]) == 46:
            pass
        else:
            is_str = True
        i -= 1
    return is_str


def check_host(host):
    try:
        if check_str_type(host):
            return sock.gethostbyname(host.decode()).encode()
    except sock.gaierror:
        return 0


with sock.socket(sock.AF_INET, sock.SOCK_DGRAM) as dns_sock:
    dns_sock.bind(("127.0.0.1", 1053))
    while True:
        data, address = dns_sock.recvfrom(1024)
        print(f"Подключение с {address} установлено")
        print(f"Запрос клиента: {data.decode()}")
        result = check_host(data)
        if result:
            dns_sock.sendto(result, address)
        else:
            dns_sock.sendto(b"Unable to locate " + data, address)




