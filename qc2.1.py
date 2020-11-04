import random
c= int(random.randint(0,10))
a=(input("hola, ¿Cual es tu nombre?: "))
print("\nHola, ",a,)
print("Vamos a jugar a parells o senars: ")
b=int(input("Escoge: \n1)par \n2)inpar\n"))
if b<1 or b>2:
  print("no se que has escogido")
d=int(input("escoge un numero del 0 al 10: "))
e=d+c
if e%2==0 and d==1:
  print("el numero que ha salido es par: ",e,"\n",a," has ganado""\nla maquina ha sacado: ",c)
elif e%2==1 and d==2:
  print("el numero que ha salido es inpar: ",e,"\n",a," has ganado""\nla maquina ha sacado: ",c)
else:
  print(a,"has perdido",", la suma que ha salido es: ",e,"\nla maquina ha sacado: ",c)
if b==3:
  print()
if d>10 or d<0:
  print("No tienes dedos para jugar")