print("tienes que escoger una de las siguientes tres opciones:")
print(" a) hoy hace un dia soleado")
print(" b) hoy hace un dia nublado")
print(" c) hoy llueve")
r=(input("¿que letra has escogido?: "))
if r == "a":
  print("has escogido que hoy hace un dia soleado")
elif r == "b":
  print("has escogido hoy hace un dia nublado")
elif r == "c":
  print("has escogido que hoy llueve")
else:
  print("esto no esta en las opciones")