fichero=open("sencillo.txt","r")
listaDePaises=list()

def lecturaArchivo():
	for linea in fichero:
		posicion=0
		alumno=[]
		for  i in range(len(linea)):
			if linea[i]==",":
				alumno.append(linea[posicion:i])
				posicion=i+2
		alumno.append(linea[posicion:-1])
		listaDePaises.append(alumno)
	print(listaDePaises)

def quitar():
	for i in listaDePaises:
		if i == "" "":
			i=i.replace("''"," ")
lecturaArchivo()

