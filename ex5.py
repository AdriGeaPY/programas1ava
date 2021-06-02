l=["polo","pito","jose","roberto"]
def bisec():
	a=input("que: ")
	for i in range(len(l)):
		if a == l[i]:
			print("la posicion de la lista en la que se encuentra tu  palabras es: ",i)
			break

bisec()
