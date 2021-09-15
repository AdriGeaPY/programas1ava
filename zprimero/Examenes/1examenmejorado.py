import random
while True:
  print("Escoge una de las siguientes opciones, poniendo su numero: \n1)Son Goku\n2)Jakie Chun\n3)Krilin\n4)Tenshinshan")
  a=int(input("¿A quien has escogido?: "))
  g=random.randint(80,90)
  j=random.randint(50,80)
  k=random.randint(20,50)
  t=random.randint(40,70)
  s=random.randint(0,80)
  if a==1:
    print("has escogido a Son Goku, tu fuerza sera de: ",g)
    print("Mr.Satan pelea con una fuerza de: ", s)
    if g>s:
      print("has ganado la batalla")
      break
    elif g==s:
      print("Has empatado la batalla")
      print("---------------------------------------------------------")
    else:
      print("Lo siento has perdido, retirate")
      break
  elif a==2:
    print("has escogido a Jakie Chun, tu fuerza sera de: ",j)
    print("Mr.Satan pelea con una fuerza de: ", s)
    if j>s:
      print("has ganado la batalla")
      break
    elif j==s:
      print("Has empatado la batalla")
      print("---------------------------------------------------------")
    else:
      print("Lo siento has perdido, retirate")
      break
  elif a==3:
    print("has escogido a Krilin, tu fuerza sera de: ",k)
    print("Mr.Satan pelea con una fuerza de: ", s)
    if k>s:
      print("has ganado la batalla")
      break
    elif k==s:
      print("Has empatado la batalla")
      print("---------------------------------------------------------")
    else:
      print("Lo siento has perdido, retirate")
      break
  elif a==4:
    print("has escogido a Tenishinshan, tu fuerza sera de: ",t)
    print("Mr.Satan pelea con una fuerza de: ", s)
    if t>s:
      print("has ganado la batalla")
      break
    elif t==s:
      print("Has empatado la batalla")
      print("---------------------------------------------------------")
    else:
      print("Lo siento has perdido, retirate")
      break
  else:
    print("No tengo ni idea de lo que has escogido")
    print("---------------------------------------------------------")
