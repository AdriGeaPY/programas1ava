import primer
a=int(input("Cuantas listas quieres comparar?: "))

def recogida():
	l=[]
	while True:
		l.append(int(input("numero: ")))
		if len(l) > a-1:
			break
	return l

lista1=recogida()
lista2=recogida()
print(lista1+lista2)

print(primer.comparar(lista1,lista2))

