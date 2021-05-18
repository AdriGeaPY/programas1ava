archivo=input("Dime el archivo que quieras abrir")
fichero=open(archivo+".txt","r")
b=fichero.read()
print(b)

def ContarPalabras():
	contar=len(b.split())
	print(contar)

def masfrecuente():
	from collections import Counter
	contar=b.split()
	contador=Counter(contar)
	frecuente= contador.most_common()[0][0]
	print("palabra mas frecuente: ", frecuente)

ContarPalabras()
masfrecuente()