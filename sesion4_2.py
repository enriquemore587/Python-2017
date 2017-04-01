def crearArchivo(nombre):
    archivo = open(nombre + '.txt', 'w')
    archivo.write('Nombre del archivo %s' %nombre)
    archivo.close()
crearArchivo('archivo1')