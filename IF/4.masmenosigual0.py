print("dime un numero: ")
numero=input()
numero1=int(numero)
print("bien, ahora dime un segundo numero: ")
numero=input()
numero2=int(numero)
if numero1-numero2 < 0:
  print("el producto de sus numeros es mas pequeño que 0")
if numero1-numero2 > 0:
  print("el producto de sus numeros es mas grande que 0")
if numero1-numero2 == 0:
  print("el producto de sus numeros es igual a 0")