import socket

socket = socket.socket()
server, port = str(raw_input('Server: ')), int(raw_input('Port: '))

msg = 'Te conectaras a: %s en el puerto %d' % (server, port)
print msg

socket.connect((server,port))
