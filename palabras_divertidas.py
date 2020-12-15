x=0
print("solo tienes dos intentos")
while True:
  var=input("Dime un palabra divertido: ")
  if var[len(var)-1] == var[0]:
    if var[1] == var[len(var)-2] and var[len(var)-1] == var[0]:
      print("Que guapa esta esta palabra, es una palabra divertida")
      break
    print("esta medio bien, pero no me convence, vuelve a intentarlo")
    x=x+1
  else:
    print("no mola tu palabra bro")
    x=x+1
  if x==2:
    print("se acabaron tus intentos, no molas")
    break