lista=list()

while True:
	nombre=input("Introduce nombre\n")
	ingrediente=input("Introduce ingrediente principal\n")
	calorias=input("Introduce calorias\n")
	dificultad=input("Introduce dificultad\n")
	explicacion=input("Introduce explicacion\n")
	lista.append([nombre,ingrediente,calorias,dificultad,explicacion])

	if len(lista)>1:
		break

for i in lista:
  for j in i:
    print(j)


a=int(input("dime que numero de receta quieres eliminar: "))
if a==1:
  print (lista[1])
elif a==2:
  print (lista[0])
else:
  print("no elimino ninguna, no se que dices")


nreceta=input("dime el nombre de la receta: ")
recetar=list()
f=False

for receta in lista:
  for dato in receta:
    if nreceta==dato:
      recetar=receta
      f=True
if f:
  print(recetar)
else:
  print("No lo he encoontrado")

# He hecho el "Actualizar un element" :)
while True:
  v=input("¿Quieres actualizar alguna de las recetas?: ")
  if v == "si":
    l = int(input(" ¿Cual de las dos recetas quieres cambiar?: "))
    k = int(input("¿Que elemento de la lista quieres cambiar?: "))
    p = input("Que es lo que quieres intercambiar: ")
    lista[l-1][k-1] = p
    print(lista)
    break
  elif v=="no":
    print("Muy bien, adios")
  else:
    print("no se que quieres decir")
    continue