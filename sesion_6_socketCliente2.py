import socket

socket = socket.socket()

server, port = str(raw_input('Server: ')), int(raw_input('Port: '))

msg = 'Te conectaras a: %s en el puerto %d' % (server, port)

print msg

socket.connect((server,port))
### 			ya existe una conexion
msg2 = raw_input('TU: ')
socket.send(msg2)




recibido = socket.recv(1024)
print 'el Server dice:  %s' % recibido
socket.close()
