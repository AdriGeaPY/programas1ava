general=[]
def datos():
	fichero=open("trabajadores.csv","r")
	for i in fichero:
		i = i.replace('"', '')
		general.append(i.split(','))

		for i in general:
			for j in range(len(i)):
				#print(i[j])
				try:
					i[j]=float(i[j])
				except:
					pass
		
	print(general)

datos()
