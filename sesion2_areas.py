'''
se requiere un programa en python que le de a escojer al usuario que area quiere calcular.

puede ser:
	*circulo
	*triangulo
	*cuadrado

posterior a que eliga el usuario que area quiere calcular, procedera a leer los requerimientos necesarios.

formulas:
	circulo -> pi * radio **2
	cuadrado -> lado por lado
	triangulo -> (base * altura) / 2
'''


#			mandamos mensaje de opciones
print ''' 
opciones a elegir 
1:calculo de un triangulo
2:calculo de un cuadrado
3:calculo de circulo
'''

#		leemos la opcion & la convertimos en entero
opcion = int(raw_input ('dame lo que quieres calcular'))


#validamos si la opcion fue 1 = Triandulo
if opcion == 1:
	#		leemos la altura
	altura = float(raw_input ('dame la altura'))
	
	#		leemos la base
	base = float(raw_input ('dame la base'))
	
	#		calculamos
	operacion= (base*altura)/2

	#		imprimimos resultado
	print 'el area de un triangulo es : %f' %(operacion)
	
	
	
elif opcion == 2:
	lado = float(raw_input ('dame un lado'))
	 
	operacion= lado*lado

	print 'el area de un cuadrado es : %f' %(operacion)
	
elif opcion == 3:
	pi= 3.1416

	radio = float(raw_input ('dame el radio'))
	 
	operacion= pi*(radio**2)

	print 'el area de un circulo es : %f' %(operacion)
else:
	print 'Numero invalido'

