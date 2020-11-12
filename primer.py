import random
a=(input ("Hola, ¿como te llamas?: "))
print("vale,",a,". Dime que quieres escoger:\n1)piedra\n2)papel\n3)tijeras ")
while True:
  c=random.randint(1,3)
  b=int(input("¿Que has escogido?: "))
  if b==1 and c==2:
    print("La maquina ha sacado: papel")
    print("lo siento, ",a," has perdido")
    c=input("Quieres volver a jugar?: ")
    if c=="si":
      print("Al Ataque, soldado: ",a)
      continue
    else:
      print("nos vemos pronto",a)
  elif b==2 and c==3:
    print("La maquina ha sacado: tijeras")
    print("lo siento, ",a," has perdido")
    c=input("Quieres volver a jugar?: ")
    if c=="si":
      print("Al Ataque, soldado",a)
      continue
    else:
      print("nos vemos pronto",a)
  elif b==3 and c==1:
    print("La maquina ha sacado: piedra")
    print("lo siento, ",a," has perdido")
    c=input("Quieres volver a jugar?: ")
    if c=="si":
      print("Al Ataque, soldado",a)
      continue
    else:
      print("nos vemos pronto",a)
  elif b==c:
    print("EmpateeEeeEee, hay que seguir jugando")
  elif b<1 or b>3:
    print ("no te entiendo",a)
    continue
  else:
    print("La maquina a sacado: ",c)
    print("has ganado,",a," fenomeno")
    c=input("Quieres volver a jugar?: ")
    if c=="si":
      print("Al Ataque, soldado",a)
      continue
    else:
      print("nos vemos pronto",a)
      break