nombres = [] #declaramos el arreglo

while True: #iniciamos un ciclo infinito
  nombre = raw_input("Escribe un nombre: ") #capturamos el nombre
  if nombre == 'fin': #SI ES FIN
       print nombres
       #print 'Finish Him' # imprimes finish Him
       break# rompes el ciclo
  #else:# SI NO!
  nombres.append(nombre) #almacenas el valor dentro del arreglo