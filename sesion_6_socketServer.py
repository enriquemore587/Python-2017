import socket

puerto = int(raw_input('Indica el puerto al que deceas apropiarte: '))

print 'Creacion del Servidor'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print 'Servidor creado'

print 'Seva a apropiar del puerto'

s.bind(("", puerto))

print 'Se apropio del puerto %d' % puerto

print 'Indicamos el numero de clientes que vamos a contestar'

s.listen(1)

print 'El servidor esta esperando a que se conecte alguien.'
sc, addr = s.accept()

print 'Imprimimos el socket que se conecto'
print sc
print 'Mostramos la direccion de quiens e conecto'
print addr
print 'Cerramos el socket cliente'
sc.close()
print 'Cerramos el socket server'
s.close()







