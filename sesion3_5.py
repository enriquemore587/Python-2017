count = 1
while count <=2:
    matricula = raw_input('Matricula: ')
    nombre = raw_input('Nombre: ')
    edad = raw_input('Edad: ')
    carrera = raw_input('Carrera: ')
    calificacion = raw_input('calificacion: ')

    dato = '%s, %s, %s, %s, %s\n' % (str(matricula), str(nombre), str(edad), str(carrera), str(calificacion))

    archivo = open('alumnos.txt', 'a')
    archivo.write(dato)
    archivo.close()
    count = count + 1

