
fichero=open("a1.txt","r")
b=fichero.read()


def ContarPalabras():
	contar=len(b.split())
	fichero=open("a2.txt","w")
	a = "el numero de palabras es "+str(contar) + "\n"
	fichero.write(a)
	fichero.close()
	
def se_repite(lista):
	frecuencia = []
	for w in lista:
		frecuencia.append(lista.count(w))
	print(frecuencia)
	input()
	a = frecuencia.index(max(frecuencia))
	c = "la palabra que mas se repite es: " + lista[a]
	fichero=open("a2.txt","a")
	fichero.write(c)
	fichero.close()
ContarPalabras()
se_repite(b.split())
