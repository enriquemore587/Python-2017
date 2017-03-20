'''
Este programa calcula el area 
de un triangulo dependiendo 
de los valores que introduce el usuario

'''

print 'Hola voy a calcular el area de un triangulo'

base = float( raw_input('Introduce la base de tu triangulo: '))
altura = float( raw_input ('Introduce la altura: ') )

area = (base * altura) / 2

print 'La base de tu triangulo fue %.3f \n la altura %.3f \n y tu area es %.3f' % (base, altura, area)
