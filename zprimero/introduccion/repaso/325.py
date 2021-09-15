def puntos(a,b):
	k=0
	for j in range(b):
		c=input("que caracteres quieres: ")
		for i in a:
			if c == i:
				k=k+1
		for h in range(j):
			print("se repite ",k,"veces el caracter ",c)
	return h

texto = input("pon una oracion: ")
signo = int (input("cuantos signos quieres contar: "))

print (puntos(texto,signo))