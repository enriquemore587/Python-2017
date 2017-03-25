nombres = [] #declaramos el arreglo

while True: #iniciamos un ciclo infinito
  nombre = raw_input("Escribe un nombre: ") #capturamos el nombre
  if nombre == 'fin': #SI ES FIN
       print nombres
       #print 'Finish Him' # imprimes finish Him
       break# rompes el ciclo
  #else:# SI NO!
  nombres.append(nombre) #almacenas el valor dentro del arreglo

'''
n = 0 #inicias la variable en cero
while n < nombres.__len__(): # iniciamos el ciclo
    #el parametro "_len_()" 
    # CUENTA LOS VALORES DENTRO DEL ARREGLO NOMBRES
    print nombres[n]# muestras el valor de cada posicion menor
    #a nombres._len_()
    n = n + 1#aumentamos la variable n 
'''