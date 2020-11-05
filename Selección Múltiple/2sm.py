print("convertidor entre medidas: ")
print("a) km a Millas nauticas")
print("b) km a Millas terrestres")
print("c) millas nauticas a km")
print("d) millas terrestres a km")
r=(input("¿Que te gustaria realizar?"))
if r == "a":
  a=float(input("¿cuantos kilometros tienes?"))
  print("el resultado es: ", a*0.54, "millas nauticas")
elif r == "b":
  b=float(input("¿cuantos kilometros tienes?: "))
  print("el resultado es: ", b*0.6214,"millas terrestres")
elif r == "c":
  c=float(input("¿cuantas millas nauticas tienes?: "))
  print("el resultado es: ", c*1.852, "kilometros" )
elif r == "d":
  d=float(input("¿cuantas millas terrestres tienes?: "))
  print("el resultado es: ", d*1.609344, "millas terrestres")
else:
  print("estos datos no son compatibles")