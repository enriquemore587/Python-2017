count = 0
while count <= 10:
	archivo = open('archivo.txt', 'a')
	archivo.write(str(count)+"\n")
	count = count + 1
	archivo.close()
