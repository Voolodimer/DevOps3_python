#!/usr/bin/python3

# Написать dns сервер.
# Сервер должен принимать соединения по протоколу udp.
# Если приходит запрос "domain.name" должен отправлять в ответ ip адрес.
# * Доп задание: иметь возможность переопределять записи клиентами:
# * ADD my.google.com:228.228.228.228

import socket as sock

user_domains = {}


def check_str_type(host):
    # Проверяем состоит ли запрос из ip-адреса или из текста
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


def check_response(user_request):
    # тип запроса: выдать IP или добавить запись
    # Пример запроса: ADD my.google.com:228.228.228.228
    # Если добавили запись return 2, если не удалось добавить return 0
    # Если есть запись в user_domains return 1
    if user_request.decode().lower().startswith('add '):
        try:
            domain, address = user_request.decode().split()[1].split(':')
            user_domains[domain] = address
            # print(user_domains)
            return 2
        except:
            return 0
    else:
        if user_request.decode() in user_domains:
            return 1


def check_host(host):
    try:
        if check_str_type(host):
            if check_response(host) == 2:
                return 2
            elif check_response(host):
                return user_domains[host.decode().lstrip()].encode()
            else:
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
        if result == 2:
            dns_sock.sendto(b"Data added successfully " + data, address)
        elif result:
            dns_sock.sendto(result, address)
        else:
            dns_sock.sendto(b"Unable to locate " + data, address)
