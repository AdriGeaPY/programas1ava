numeco=int(input("¿Cuantas veces quieres que se repita el eco?: "))
while True:
  repeticion=(input("\n¿Que quieres decir?: "))
  if repeticion == "Adéu" or repeticion == "ADÉU" or repeticion=="adéu":
    print("Adéu, que tengas un buen dia")
    break
  for i in range (numeco):
    print(repeticion,"", end='')
