import ipaddress

print('--imprimir o ip--')
ip = '192.168.0.1'
endereco = ipaddress.ip_address(ip)
print(endereco + 2300)

print('-'*30)

print('--imprimir a rede--')
ip2 = '192.168.0.0/24'
rede = ipaddress.ip_network(ip2)
print(rede)

print('-'*30)

print('--rede do ip colocado--')
ip3 = '192.168.0.100/24'
rede = ipaddress.ip_network(ip3, strict=False)
print(rede)

print('-'*30)

print('--ips na rede--')
ip4 = '192.168.0.100/30'
rede = ipaddress.ip_network(ip4, strict=False)
for ip in rede:
    print(ip)