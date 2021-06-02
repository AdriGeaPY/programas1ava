file = open('completo.txt', 'r').readlines()


paises = []

def recogida():
	for i in file:
		i = i.replace('"', '')
		paises.append(i.split(','))
		#print(i)


	for i in paises:
		for j in range(len(i)):
			#print(i[j])
			try:
				i[j]=float(i[j])
			except:
				pass
	#print(paises)


def usuario():
	r=input("¿De que pais quieres saber los datos?: ")
	c=input("Como quieres recibir los datos?: \n1--> Por pantalla\n2--> Generar archivo\n")
	for i in paises:
#		r=input("¿De que pais quieres saber los datos?: ")
		
		if c=="1":
			if r == i[1]:
				print("El país seleccionado es:",i[1],"\nCodigo del pais: ",i[0],"\nContinente: ",i[2],"\nRegion: ",i[3],"\nSuperficie: ",i[4],"\nIndepYear: ",i[5],"\nPoblación: ",i[6],"\nEsperanza de vida: ",i[7],"\nPIB: ",i[8],"\nPIB antiguo: ",i[9],"\nNombre Local: ",i[10],"\nForma de govierno: ",i[11],"\nJefe de Estado: ",i[12],"\nCapital: ",i[13],"\nCodigo2: ",i[14])
				break
		elif c=="2":
			if r== i[1]:
		#for i in paises:
				
				#texto=("El país seleccionado es:",i[1],"\nCodigo del pais: ",i[0],"\nContinente: ",i[2],"\nRegion: ",i[3],"\nSuperficie: ",i[4],"\nIndepYear: ",i[5],"\nPoblación: ",i[6],"\nEsperanza de vida: ",i[7],"\nPIB: ",i[8],"\nPIB antiguo: ",i[9],"\nNombre Local: ",i[10],"\nForma de gobierno: ",i[11],"\nJefe de Estado: ",i[12],"\nCapital: ",i[13],"\nCodigo2: ",i[14])
					
				fichero = open(i[0]+ ".txt","w")			
				fichero.write("El país seleccionado es: "+str(i[1])+"\nCodigo del pais: "+str(i[0])+"\nContinente: "+str(i[2])+"\nRegion: "+str(i[3])+"\nSuperficie: "+str(i[4])+"\nIndepYear: "+str(i[5])+"\nPoblación: "+str(i[6])+"\nEsperanza de vida: "+str(i[7])+"\nPIB: "+str(i[8])+"\nPIB antiguo: "+str(i[9])+"\nNombre Local: "+str(i[10])+"\nForma de gobierno: "+str(i[11])+"\nJefe de Estado: "+str(i[12])+"\nCapital: "+str(i[13])+"\nCodigo2: "+str(i[14]))
				fichero.close()

def continente():
	q=input("¿De que continente quieres saber la informacion?: ")
	c=input("Como quieres recibir los datos?: \n1--> Por pantalla\n2--> Generar archivo\n")
	poblacion=0
	superficie=0
	espia=True
	if c == "1":
		print("Todos los paises que estan en este continente son: ")
		for i in paises:
			for j in range(len(i)):
				if q == i[2]:
					espia=False
					try:	
						poblacion=poblacion+int(i[6])
						superficie=superficie+int(i[4])
						print(i[1])
						break
					except:
						continue
		print("La poblacion total es: ",poblacion,"habirantes")
		print("La superfice total es: ",superficie,"km²")
	elif c == "2":
		for i in paises:
			for j in range(len(i)):
				try:
					if q == i[j]:
						espia= False	
						poblacion=poblacion+int(i[6])
						superficie=superficie+int(i[4])
						archivo=open(q+".txt","a")
						archivo.write(i[1] + "\n")
						archivo.close()
				except:
					continue
		archivo=open(q+".txt","a")
		archivo.write("poblacion: " + str(poblacion) +" habitantes" + "\nsuperficie: " + str(superficie)+ " km²")
		archivo.close()
	else:
		print("pon algo que sepa lo que es")
		
	if espia:
		print("No te entiendo")

def esperanza():
	c=input("Como quieres recibir los datos?: \n1--> Por pantalla\n2--> Generar archivo\n")
	q="{:.2f}".format(float(input("Que renta por capita buscas?: ")))
	e=float(input("Que esperanza de vida buscas?: "))
	espia= True
	for i in range(len(paises)):
		try:
			if "{:.2f}".format(float(paises[i][8]/paises[i][6])) == q:
				
				if e == paises[i][7]:
					espia= False
					if c == "1":
						print(paises[i][1])
					elif c == "2":
						fichero=open("esperanza y renta"+".txt","a")
						fichero.write("el pais que buscas:\n"+paises[i][1])	
						fichero.close()	
					else:
						print("pon algo que entienda")
		except:
			continue
		
	if espia:
		print("No hay ningun pais coincidente")
	

k=int(input("Que es lo que quieres ver:\n1--> Datos de un pais en concreto\n2--> Informacion sobre un continente\n3--> Espereanza de vida de un pais\n¿Que escoges?: "))

recogida()

if k == 1:
	usuario()
elif k == 2:
	continente()
elif k == 3:
	esperanza()
else:
	print("esperaba mas de ti.")


#"Code","Name","Continent","Region",SurfaceArea,IndepYear,Population,LifeExpectancy,GNP,GNPOld,"LocalName","GorvernmentForm","HeadOfState","Capital","Code2"