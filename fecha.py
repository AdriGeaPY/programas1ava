print("dime un dia del año (numero): ")
numero=input()
dia=int(numero)
print("ahora dime un mes del año (numero)")
mes=input()
mes=int(mes)
print("por ultimo, dime un año")
año=input()
año=int(año)
if dia <= 30 and mes <= 12:
  print("esta fecha es correcta")
if dia > 30 or mes>12:
  print("esta no es una fecha valida")
if dia < 0 or mes < 0 or año < 0:
  print("esta no es una fecha valida")