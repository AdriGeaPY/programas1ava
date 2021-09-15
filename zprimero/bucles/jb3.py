import random
g=0
p=0
while True:
  a=int(input("¿Cuantos chinos habran? (0-6): "))
  b=int(input("¿Cuantos chinos coges? (0-3): "))
  c=random.randint(0,3)
  print("La maquina tiene: ",c)
  if a == b+c:
    print("Has ganado fiera")
    g=g+1
    d=input("¿Quieres seguir jugando?: ")
    if d=="si":
      print("Tu puntuacion total es de: ",g,"ganadas y ",p,"perdidas")
      print("perfecto, continua")
      continue
    else:
      print("Tu puntuacion final es de: ",g,"ganadas y ",p,"perdidas")
      print("Muy bien adios.")
      break
  elif a < 0 or a > 6:
    print("no te entiendo")
    continue
  elif b < 0 or b > 3:
    print("no te entiendo")
    continue
  else:
    print("Has perdido, matao")
    p=p+1
    d=input("¿Quieres seguir jugando?: ")
    if d=="si":
      print("Tu puntuacion total es de: ",g,"ganadas y ",p,"perdidas")
      print("perfecto, continua")
      continue
    else:
      print("Tu puntuacion final es de: ",g,"ganadas y ",p,"perdidas")
      print("Muy bien adios.")
      break