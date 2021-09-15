
a=int(input("Cuantas listas quieres comparar?: "))
def recoger():
	l=list()
	for i in range(2):
		l.append(int(input("numero: ")))
	return l

listagen=list()
for j in range(a):
	listagen.append(recoger())


def comparar(a,b):
	for u in a:
		for p in b:
			if u == p:
				return "cierto"
	return"falso"