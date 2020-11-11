import random
a=(input ("Hola, ¿como te llamas?: "))
print("vale,",a,". Dime que quieres escoger:\n1)piedra\n2)papel\n3)tijeras ")
b=int(input("¿Que has escogido?: "))
c=random.randint(1,3)
while True:
  if b==1 and c==2:
    print("La maquina ha sacado: papel")
    print("lo siento, ",a," has perdido")
    break
  elif b==2 and c==3:
    print("La maquina ha sacado: tijeras")
    print("lo siento, ",a," has perdido")
    break
  elif b==3 and c==1:
    print("La maquina ha sacado: piedra")
    print("lo siento, ",a," has perdido")
    break
  elif b==c:
    print("EmpateeEeeEee, hay que seguir jugando")
  elif b<1 or b>3:
    print ("no te entiendo")
  else:
    print("has ganado,",a," fenomeno")
    break