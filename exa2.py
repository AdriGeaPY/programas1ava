general=[]
def datos():
	fichero=open("trabajadores.csv","r")
	for i in fichero:
		i = i.replace('"', '')
		general.append(i.split(','))

		for i in general:
			for j in range(len(i)):
				try:
					i[j]=float(i[j])
				except:
					pass
		
	#print(general)

def salario():
	suma=0
	for i in general:
		suma=suma+i[5]
		todos = len(general)
		
		medio=suma/todos
	print("la media de todos los salarios es: ",medio)

datos()
salario()