def recogida():
	l=[]
	for i in range(2):
		l.append(int(input("numero: "+str(var))))
	return l

def comparar(a,b):
	for i in a:
		for j in b:	
			if i == j:
				return True
	return False

ListaGeneral = []
NumListas = int (input("¿Cuántas listas quieres comparar?"))

#Recogida de datos
for var in range(NumListas):
	ListaGeneral.append(recogida())

#Comparación Listas
for i in range(len(ListaGeneral)):
	for j in range(i+1 , len(ListaGeneral)):
		if comparar(ListaGeneral[i] , ListaGeneral[j]):
			print("Hay coincidencia")
			(exit)
		else:
			print("false")
			(exit)

----------------------


matricula = open("segundo.csv" , "r")
lista = matricula.readlines()



def crear():
	for linea in lista: 
		a = linea.split(",")
		archivo = open(a[0] + ".md" , "w")
		archivo.write("## " + a[0] + " Ha sido matriculado en: \n-" + "\n-".join(a[1:]))
		archivo.close()

		
crear()