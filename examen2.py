lista=list()

def media():
	for alumno in lista:
		var=0
		for posicion in alumno[1:]:
			var=var+posicion
		print("corredor "+alumno[0])
		media=var/4
		print(media)
		print(var/len(alumno[1:]))

def Existe(nombre,nota):
	for fila in lista:
		if fila[0]==nombre:
			fila.append(nota)
			return False
	return True
		
		
def lecturaArchivos():
	fichero=open("a1.txt","r").read()
	for fila in fichero:	
		for i in range(len(fila)):
			if fila[i]==" ":
				lista.append(fila[0:i])
				


lecturaArchivos()
print(lista)

media()