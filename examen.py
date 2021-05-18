fichero=open("archivo.txt","r")
a=fichero.read()
print(a)

''''
def media():
	lista=list()
	for i in fichero:
		for j in range(len(i)):
			lista.append(j)
	print(lista)

media()
'''
lista=list()

def media():
	for corredor in lista:
		var=0
		for posicion in corredor[1:]:
			var=var+posicion
		print("corredor "+corredor[0])
		media=var/3
		print(media)
		print(var/len(corredor[1:]))

def Existe(nombreCorredor,posicion):
	for fila in lista:
		if fila[0]==nombreCorredor:
			fila.append(posicion)
			return False
	return True

def lecturaArchivos():
	fichero=open("archivo.txt","r")
	for fila in fichero:	
		for i in range(len(fila)):
			lista.append([fila[0:i],int(fila[i+1:])])
			if fila[i]==" " and Existe(fila[0:i],int(fila[i+1:])):
				lista.append([fila[0:i],int(fila[i+1:])])

print(lista)
media()

