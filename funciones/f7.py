import primer
def recogida():
	l=[]
	while True:
		l.append(int(input("numero: ")))
		if len(l) > 2:
		 break
	return l

lista1=recogida()
lista2=recogida()
print(lista1+lista2)

print(primer.comparar(lista1,lista2))
