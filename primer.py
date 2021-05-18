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
		elif c=="2":
			if r== i[1]:
		#for i in paises:
				
				#texto=("El país seleccionado es:",i[1],"\nCodigo del pais: ",i[0],"\nContinente: ",i[2],"\nRegion: ",i[3],"\nSuperficie: ",i[4],"\nIndepYear: ",i[5],"\nPoblación: ",i[6],"\nEsperanza de vida: ",i[7],"\nPIB: ",i[8],"\nPIB antiguo: ",i[9],"\nNombre Local: ",i[10],"\nForma de gobierno: ",i[11],"\nJefe de Estado: ",i[12],"\nCapital: ",i[13],"\nCodigo2: ",i[14])
					
				fichero = open(i[0]+ ".txt","w")			
				fichero.write("El país seleccionado es: "+str(i[1])+"\nCodigo del pais: "+str(i[0])+"\nContinente: "+str(i[2])+"\nRegion: "+str(i[3])+"\nSuperficie: "+str(i[4])+"\nIndepYear: "+str(i[5])+"\nPoblación: "+str(i[6])+"\nEsperanza de vida: "+str(i[7])+"\nPIB: "+str(i[8])+"\nPIB antiguo: "+str(i[9])+"\nNombre Local: "+str(i[10])+"\nForma de gobierno: "+str(i[11])+"\nJefe de Estado: "+str(i[12])+"\nCapital: "+str(i[13])+"\nCodigo2: "+str(i[14]))
				fichero.close()
		'''
		elif r != i[1]:
			s=input("Algo no funciona bien,\n¿Has escrito el nombre con la primera en mayuscula y en ingles?\n¿Si o no?: ")
			
			if s == "no":
				print("Corrigelo")
				continue
			elif s=="si":
				print("vuelve a ejecutar el programa :(")
		'''

recogida()
usuario()

#"Code","Name","Continent","Region",SurfaceArea,IndepYear,Population,LifeExpectancy,GNP,GNPOld,"LocalName","GorvernmentForm","HeadOfState","Capital","Code2"