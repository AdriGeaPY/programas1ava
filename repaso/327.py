def puntos(a,b):
	k=0
	l=list()
	for j in range(b):
		c=input("que caracteres quieres: ")	
		for i in a:
			if c == i:
				k=k+1
		p=("se repite ",k,"veces el caracter ",c)
		l.append(p)
	return l

texto = input("pon una oracion: ")
signo = int (input("cuantos signos quieres contar: "))

print (puntos(texto,signo))

#las k se me suman en vez de que el contador vuelva a 0
'''
No entiendo el problema. Yo lo veo todo bien. He probado varias veces y el programa funciona correctamente....
Ya me dirás
'''