import math

def area_circulo(radio):
	return radio*radio*math.pi

radio=int(input("radio: "))
print ("el area es: ",round(area_circulo(radio)))