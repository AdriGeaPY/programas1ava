x=0
while True:
  a=input("Escribe un texto (minimo 20 palabras): ")
  b=a.count(" ")+1
  if a.count(" ") < 19:
    x=x+b
    print("Llevas: ",x,"Te faltan: ",20-x,"\nno me sirve, sigue escribiendo")
    continue
  else:
    print("Muy bien, ya has acabado")
    break