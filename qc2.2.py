import random
a=str(input("Dime tu nombre: "))
print("""
1) par
2) inpar
""")
b=int(input("¿Que es lo que quieres?"))
c=int(input("dime un numero que del 0 al 10: "))
d=random.randint(0,10)
if b==1:
  if (c+d)%2==0:
    print(a,"has ganado")
  elif (c+d)%2!=0:
    print(a,"has perdido")
elif b==2:
  if (c+d)%2==0:
    print(a,"has perdido")
  elif (c+d)%2!=0:
    print(a,"has ganado")
else:
  print("mal") 