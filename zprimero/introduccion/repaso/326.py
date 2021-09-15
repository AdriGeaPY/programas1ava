def puntos(a,b):
	k=0
	l=list()
	for l in range(b):
		c=input("que caracteres quieres: ")
		print("se repite ",k,"veces el caracter ",c)
	for i in a:
		if c == i:
			k=k+1
	return 

texto = input("pon una oracion: ")
signo = int (input("cuantos signos quieres contar: "))

print (puntos(texto,signo))