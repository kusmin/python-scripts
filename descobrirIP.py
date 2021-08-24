import socket as s

host = 'blogdopensadormoderno.com.br'

ip = s.gethostbyname(host)

print('O IP do Host "' + host + '" é:' + ip)
