
print("Introduce la base del rectangulo")
base=input()
base=int(base)
print("introduce la altura del rectangulo")
altura=input()
altura=int(altura)
print("el area es", base * altura ,"m2")
print("Ahora vamos a calcular el area y el perimetro de una circunferencia, introduce el radio:")
radio=input()
radio=int(radio)
import math
print("el area es: ", math.pi * radio * radio,)
print("el perimetro es:", 2 * math.pi * radio)