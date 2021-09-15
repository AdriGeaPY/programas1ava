lista=list()

def lecturaArchivos(file):
	fichero=open(file,"r")
	for i in fichero:
		lista.append(i)

for j in [1,2,3]:
	lecturaArchivos("a"+str(j)+".txt")

print(lista)