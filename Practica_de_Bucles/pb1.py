import random
print("Adivina el numero del 0 al 9")
while True:
  a=random.randint(0,9)
  b=int(input("Dime el numero: "))
  if a==b:
    print("Lo has acertado, IDOLO")
    c=input("¿Quieres jugar otra vez?: ")
    if c=="si":
     continue
    else:
     print("Adios.")
     break
  if b<0 or b>9:
    print("no esta dentro del juego")
    continue
