x=0
p=0
print("solo tienes dos intentos")
while True:
  var=input("Dime un palabra divertida: ")
  if var[:2] == var[2:] and var[1:] == var[:1]:
    p=p+3
    print("capicua de dos letras (+3)", "\n tu puntuacion es: ",p)
  elif var[:1].isnumeric() == var[1:].isnumeric() and var[:2].isnumeric() == var[2:].isnumeric():
    p=p+2
    print("capicua de dos numeros (+2)","\n tu puntuacion es: ",p)
  elif var[1].isnumeric() == var[len(var)-2].isnumeric() and var[len(var)-1].isnumeric() == var[0].isnumeric() and var[2].isnumeric() == var[len(var)-3].isnumeric():
    p=p+3
    print("capicua de tres numeros (+3)","\n tu puntuacion es: ",p)
  elif var[1] == var[len(var)-2] and var[len(var)-1] == var[0] and var[2] == var[len(var)-3] and var[2] == var[len(var)-4]:
    p=p+4
    print("capicua de tres letras (+4)","\n tu puntuación es: ",p)
  elif var[1:] == var[:99]:
    p=p+5
    print("nom palindrom (+5)","\n tu puntuacion es: ",p)
  elif var[0:].isnumeric() and var[:99].inumeric():
    p=p+5
    print("nombre palindrom (+5)","\n tu puntuacion es: ",p)
  else:
    print("no mola tu palabra bro")
    x=x+1
    if x==2:
      print("se acabaron tus intentos, no molas")
      break
  