a=int(input("dime lo que mide el primer lado: "))
b=int(input("¿cuanto vale el segundo lado?: "))
c=int(input("y por ultimo, ¿cuanto vale el tercer lado?: "))
if a<=b+c and b<=a+b and c<=b+a:
  print("no es un triangulo")
else:
  print("es un traingulo")