import random
import time 
while True:
  a=random.randint(1,12)
  a2=random.randint(1,12)
  b=a
  time.sleep(1)
  print("lo que has sacado es: ",b)
  c=a2
  time.sleep(1)
  print("lo que yo he sacado es: ",c)
  if b<c:
    print("Has ganado")
    break
  elif b==c:
    print("Empateee")
    print("----------------------------------------------------------------")
  else:
    print("has perdido")
    print("----------------------------------------------------------------")