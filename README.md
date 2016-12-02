# Python-Graficas
#Extracción, graficación, exportación(csv), creacion PDF sencillo(por medio de un arreglo de imagenes de DISCO)


#CREACION DE PDF POR MEDIO DE IMAGENES DE DISCO

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image
doc = SimpleDocTemplate("final.pdf", pageSize=letter)
images = [Image("./IMG1.png"),Image("./IMG2.png"),Image("./IMG3.png"),Image("./IMG4.png"),Image("./IMG5.png")]
doc.build(images)

#Ajuste tamaño imagenes
def imagenes(nombre):
	from PIL import Image
	imageFile = "./"+nombre+".png"
	im1 = Image.open(imageFile)
	width = 500
	height = 420
	im2 = im1.resize((width, height), Image.NEAREST)
	im2.save(nombre+".png")
	return im2

#CONEXION BASE DE DATOS
def conexion(tabla):
	import MySQLdb
	db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="analisis")
	cursor = db.cursor()
	recs = cursor.execute("SELECT * FROM " + tabla + " ;")
	respuesta = []
	for x in range(recs):
		respuesta.append( str( cursor.fetchone() ) )
	return respuesta

#CREACION TABLA MATPLOTLIB
def creacion_tabla(frecuencia):
	import matplotlib.pyplot as plt
	tabla = conexion(frecuencia)#FUNCION CONEXION BASE DE DATOS
	for i in range(len(tabla)):
		tabla[i] = str(tabla[i]).split(",")
	plt.table(cellText=tabla, rowLabels=range(len(tabla)), colLabels=tabla[0], loc='upper center')
	plt.savefig(frecuencia + ".png")
	plt.show()
  
  
#CREACION DE GRAFICAS  MATPLOTLIB
# x - y son arreglos
#se puede agregar nombre a las etiquetas de los ejes con <plt.xlabel=('nombre de X')   plt.ylabel=('nombre de Y')>
def grafica(x,y,nombre):
    import matplotlib.pyplot as plt
    if str(nombre)=='DISPERSION':     #grafica de dispersion
        plt.title(nombre)
        plt.plot(x, y, 'bs')  # , x, range(len(z)),  'g^',x, range(len(z)), 'g^')
        plt.savefig(nombre + ".png")
        plt.show()
    else:
        plt.plot(x,y)
        plt.title(nombre)
        plt.savefig(nombre + ".png")
        plt.show()
        
 #LECTURA Y ESCRITURADE ARCHIVOS .csv
 
 def leerFrecuencia():
    file = open('archivo.csv', 'r')
    archivo = file.readlines()
    file.close()
    for a in archivo:
        data= str(a)
        data=data.split(",")
    return data

def guardarArchivo(nombre,line):
    saveFile = open(nombre+'.csv', 'a')
    saveFile.write(line)
    saveFile.write('\n')
    saveFile.close()
