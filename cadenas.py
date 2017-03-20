#!/usr/bin/env python
# -*- coding: utf-8 -*-

##################################################################
#
#
#			https://github.com/enriquemore587/Python-2017
#
#
##################################################################

cadena = 'ingenieria en Sistemas Computacionales'

'''
Método: capitalize()

Retorna: una copia de la cadena con la primera letra en mayúsculas.

print cadena.capitalize() 
'''



'''
Método: lower()

Retorna: una copia de la cadena en minúsculas.
print cadena.lower()
'''

'''
Método: upper()

Retorna: una copia de la cadena en mayúsculas.

print cadena.upper()
'''

'''
Método: swapcase()

Retorna: una copia de la cadena convertidas las mayúsculas en minúsculas y viceversa.

print cadena.swapcase()
'''


'''
Método: center(longitud[, "caracter de relleno"])

Retorna: una copia de la cadena centrada.

print cadena.center(50, "=") 
'''


'''
Método: count("subcadena" [, posicion_inicio, posicion_fin])

Retorna: un entero representando la cantidad de apariciones de subcadena dentro de cadena.

'''



'''
Método: startswith("subcadena" [, posicion_inicio, posicion_fin])

Retorna: True o False

print cadena.startswith("inge") 

print cadena.startswith("en", 14) 



cadena = 'hola como'
print cadena.startswith("co", 5) 
'''


##############################################
#				sustitucion

'''
Método: format(*args, **kwargs)

Retorna: la cadena formateada.


cadena = "Hola me llamo {0}" 
print cadena.format("enrique")
'''


'''
Eliminar caracteres a la izquierda y derecha de una cadena

Método: strip(["caracter"])

Retorna: la cadena sustituida.

cadena = ' https://github.com/enriquemore587/Python-2017  '
print cadena.strip(' ')

'''


'''
Eliminar caracteres a la izquierda de una cadena

Método: lstrip(["caracter"])

Retorna: la cadena sustituida.

cadena = ' https://github.com/enriquemore587/Python-2017  '
print cadena.lstrip("://" )
'''

'''
Unir una cadena de forma iterativa

Método: join(iterable)

Retorna: la cadena unida con el iterable (la cadena es separada por cada uno de los elementos del iterable).

'''
formato_numero_factura = ("Nº 0000-0", "-0000 (ID: ", ")") 
numero = "275" 
numero_factura = numero.join(formato_numero_factura) 
print numero_factura 

'''
Partir una cadena en tres partes, utilizando un separador

Método: partition("separador")

Retorna: una tupla de tres elementos donde el primero es el contenido de la cadena previo al separador, el segundo, el separador mismo y el tercero, el contenido de la cadena posterior al separador.

tupla = "https://github.com/enriquemore587/Python-2017".partition(".com") 
print tupla 


parte1, parte2, parte3 = tupla 
print "parte1: {0}\n parte2: {1}".format(parte1, parte2) 
'''


'''
Partir una cadena en en líneas

Método: splitlines()

Retorna: una lista donde cada elemento es una fracción de la cadena divida en líneas.
t
exto = """Linea 1
Linea 2
Linea 3
Linea 4
""" 
print texto
print texto.splitlines() 
'''

