import random
while True:
  random1=random.randint(1,9)
  random2= random.randint(1,9)
  print("Vamos a demostrar que no eres un robot: ")
  print(random1,"x +", random2, "=0")
  solucion=float(input("Dime cual es el resultado: "))
  if random1 * solucion + random2 >= -0.5 and random1 * solucion + random2 <= 0.5:
    print("Es correcto, no eres un robot")
    break
  else:
    print("oh no, eres un robot")
    continue