def get_edad(persona):
	return persona[1]
datos = ['Nombre', 'Edad', 'Carrera']
persona1 = ['Enrique', 22, 'Sistemas Computacionales']
persona2 = ['Mariana', 22, 'Sistemas Computacionales']

edades = []

edades.append(get_edad(persona1))
edades.append(get_edad(persona2))

print edades[0]
print edades[1]