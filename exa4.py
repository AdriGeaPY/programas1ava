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

def jefes():
	for i in general:
		try:
			if i[0] == i[3]:
				print("a")
		except:
			continue

datos()
jefes()
