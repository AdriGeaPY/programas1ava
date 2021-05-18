
listaDeLineas=list()

def Existe(nombreCorredor):
	input(" ")
	print(nombreCorredor)
	input("")
	print(listaDeLineas)
	for fila in listaDeLineas:
		for i in fila:
			if i==nombreCorredor:
				return False
			else:
				return True	
	return True
		
		
def lecturaArchivos(file):
	fichero=open(file,"r")

	for fila in fichero:
		for i in range(len(fila)):
			if fila[i]==" " and Existe(fila[0:i]):
				listaDeLineas.append([fila[0:i],fila[i:-1]])

for j in [1,2]:
	lecturaArchivos("a"+str(j)+".txt")

print(listaDeLineas)





''''
for i in range(len(listaDeLineas)-1, -1, -1):
        if listaDeLineas[i] in listaDeLineas[:i]:
            del(listaDeLineas[i])

for fila in listaDeLineas:
		for i in fila:
			if nombreCorredor:
				return False
			else:
				return True
'''
