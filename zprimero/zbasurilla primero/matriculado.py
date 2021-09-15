fichero=open("csv.txt","r")
listaDeAlumnos=list()

def lecturaArchivo():
	for linea in fichero:
		posicion=0
		alumno=[]
		for  i in range(len(linea)):
			if linea[i]==",":
				alumno.append(linea[posicion:i])
				posicion=i+2
		alumno.append(linea[posicion:-1])
		listaDeAlumnos.append(alumno)

def crear():
	for i in listaDeAlumnos:
		print(i)
		archivo=open(i[0]+".txt","w")
		archivo.write("Hola, "+i[0]+"has sido matriculado en: "+", ".join(i[1:]))
		archivo.close()

lecturaArchivo()
crear()
print(listaDeAlumnos)