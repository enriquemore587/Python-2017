barrio = []
def add_cond(directory):
    barrio.append(directory)

directorio1 = {
    'Nombre': 'Jose Enrique',
    'Casa': 1
}
add_cond(directorio1)

directorio2 = {
    'Nombre': 'Maria',
    'Casa': 24
}
add_cond(directorio1)
directorio3 = {
    'Nombre': 'Juan',
    'Casa': 65
}
add_cond(directorio3)
print barrio
print barrio[1]
print barrio[0]['Nombre']
