general=[]
def datos():
	fichero=open("trabajadores.csv","r")
	for i in fichero:
		i = i.replace('"', '')
		general.append(i.split(','))

		for i in general:
			for j in range(len(i)):
				try:
					i[j]=float(i[j])
				except:
					pass
		
	#print(general)

def salario():
	suma=0
	for i in general:
		suma=suma+i[5]
		todos = len(general)
		
		medio=suma/todos
	#print("la media de todos los salarios es: ",medio)

def crear():
	empleados=0
	vendedor=0
	director=0
	analista=0
	presidente=0
	for i in general:
		if i[2] == "EMPLEADOS":
			empleados=empleados+1
		elif i[2] == "VENDEDOR":
			vendedor=vendedor+1
		elif i[2] == "DIRECTOR":
			director=director+1
		elif i[2] == "ANALISTA":
			analista=analista+1
		elif i[2] == "PRESIDENTE":
			presidente=presidente+1
	archivo=open("funciones.txt","w")
	archivo.write("director: "+str(director)+ "\nvendedor: "+str(vendedor)+"\nempleados: "+str(empleados)+"\nanalista: "+str(analista)+"\npresidente: "+str(presidente))
	archivo.close()
#LO QUE HE RETOCADO HA SIDO QUE HE PUESTO EL STR() A LA HORA DE ESCRIBIR LOS DATOS EN EL FICHERO Y TAMBIEN LO HE ORDENADO UN POCO. TAMBIEN HE AÑADIDO DOS CATEGORIAS (ANALISTA I PRESIDENTE), QUE NO ME HABIA FIJADO PORQUE FUI MUY RAPIDO YA QUE NO TENIA TIEMPO

datos()
salario()
crear()