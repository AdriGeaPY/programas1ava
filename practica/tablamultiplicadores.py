import random
lista=[]
for i in range(1,11):
  lista.append(random.randint(1,10))
for j in lista:
  print(j,j**2,j**3)
