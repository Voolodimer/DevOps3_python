import os
import netifaces


class Router:
    def add_ip_address(self, name, ip_address, netmask):
        return os.system(f"ifconfig {name} {ip_address} netmask {netmask}")

    def del_ip_address(self, name, ip_address):
        return os.system(f"ifconfig {name} del {ip_address}")
        # ip addr del 192.168.0.77/24 dev eth0

    def show_ip_address(self):
        for iface in netifaces.interfaces():
            iface_details = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in iface_details:
                print(iface_details[netifaces.AF_INET])
                # print(iface_details[netifaces.AF_INET][0]['addr'])

    def add_ip_routes(self,ip_addr_mask, gateway):
        return os.system(f"route add -net {ip_addr_mask} via {gateway}")
        # route add -net 10.10.0.0/16 gw 10.10.1.1
        # ip route add 10.10.0.0/16 via 10.10.1.1

    def del_ip_routes(self, ip_address, netmask):
        return os.system(f"route delete -net {ip_address} netmask {netmask}")
        # route delete -net 10.10.0.0 netmask 255.255.0.0

    def show_ip_routes(self):
        return os.system("ip route")


# Router.show_ip_address(Router)
# Router.show_ip_routes(Router)