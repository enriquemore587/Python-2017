count = 0
while True:
	archivo = open('bucle.py', 'a')
	archivo.write(str(count)+"\n")
	count = count + 1
	archivo.close()
