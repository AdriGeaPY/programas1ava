archivo=input("Dime el archivo que quieras abrir")
fichero=open(archivo+".txt","r")
b=fichero.read()
print(b)

def ContarPalabras():
	contar=len(b.split())
	print(contar)


def se_repite(lista):
	frecuencia = []
	for w in lista:
		frecuencia.append(lista.count(w))
		print(frecuencia)
	a = frecuencia.index(max(frecuencia))
	print("la palabra que mas se repite es: " , lista[a])

def mostrardatos(lista):
	for h in lista:
		lista.count(h)
		print(lista)
	
ContarPalabras()
se_repite(b.split())
mostrardatos()