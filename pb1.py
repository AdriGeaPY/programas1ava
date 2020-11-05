import random
a=random.randint(0,9)
print("Adivina el numero del 0 al 9")
while True:
  b=int(input("Dime el numero: "))
  if a==b:
    print("Lo has acertado, IDOLO \nVuelve a ejecutar el programa para mas.")
    break
  elif b<0 or b>9:
    print("no esta dentro del juego\nVuelve a ejecutar el juego")
    break