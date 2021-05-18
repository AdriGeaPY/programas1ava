a=input("Pon una oración\n")
b=input("Que quieres que cuente: ")
def contar(a,b):
	o=a.count(b)
	return o
print(contar(a,b))