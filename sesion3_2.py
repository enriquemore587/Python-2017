# declaracion del arreglo con 5 elementos
arreglo1 = ["Enrique", "Uriel", "Brenda", "Daniel", "Mariana"]

# declaracion de una variable que se va a iterar
i = 0

# while i sea menor a 5  por que de esta forma al
#aumentar a i en uno dentro del while solo
#solo llegaria a 4
while i < 5:
    print "El nombre de la posicion %d es %s"%(i,str(arreglo1[i]))
    i = i + 1


for elemento in arreglo1:
    print elemento