'''
requerimientos:
agregen: 2 campos mas:
numeroAlumnos
campo maestros []


programa con una funcion que agregue: maestros

programa con una funcion que agregue: especialidad & dentro de la especialidad dos materias

'''
def add_maestro(nombreCarrera, nombreMaestro):
    pass
tese = [
    {
        'NameC': 'isc',
        'NumeroS':9,
        'esp':[]
     },

    {
        'NameC': 'Aereonautica',
        'NumeroS':7,
        'esp': []
    },

    {
        'NameC':' Mecatronica',
        'NumeroS':8,
        'esp': []
    }

]
def add_esp (nameC,esp,mat):
    tam_car_tese = len(tese)
    pos_elem = range(tam_car_tese)
    for carrera in pos_elem:
        if tese[carrera]['NameC'] == nameC:
            print tese[carrera]['esp']

add_esp('isc','redes',['redes1','redes2'])