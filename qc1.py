print("Vamos a jugar a cara o cruz, escoge un numero: ")
print("0) cara")
print("1) cruz")
a=int(input("¿Que valor escoges?"))
import random
b=random.randint(0,1)
if b == 0:
  print("ha salido: ","cara")
else:
  print("ha salido: cruz")
if a!=b and a<1  or a!=b and a>0:
  print("has perdido")
elif a==b:
  print("has ganado, CAMPEON")
if a>1 or a<0:
  print("NO ENTIENDO lo que estas poniendo")