x=0
p=0
print("solo tienes dos intentos")
while True:
  var=input("Dime una palabra divertida")
  if var[len(var)-1] == var[0]:
    if var[len(var)-2]== var[1]:
      if var[1].isnumeric() and var[0].isnumeric():
        if var[len(var)-3]== var[2]:
          if var[2].isnumeric():
            p=p+3
            print("Capicua de tres numeros (+3)","\n tu puntuacion es: ",p)
          else:
            p=p+3
            print("Capicua de 3 letras (+3)","\n tu puntuacion es: ",p)
          p=p+2
          print("Capicua de dos numeros (+2)","\n tu puntuacion es: ",p)
        print
