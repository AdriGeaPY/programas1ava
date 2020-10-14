dia=int(input("dime un dia del año"))
print("ahora dime un mes del año (letra) (en mayuscula NO)")
mes=input()
print("por ultimo, dime un año")
año=input()
año=int(año)

if dia >= 1 and dia <= 30 and (mes=="abril" or mes=="junio"or mes=="septiembre"or  mes=="noviembre"):
  print("esta fecha es correcta")

elif dia <= 0 or año < 0:
  print("esta no es una fecha valida")

elif dia > 28 and dia < 1 and (mes == "febrero"):
  print("esta fecha no es valida")

elif dia <= 31 and dia >= 1 and (mes =="enero" or mes=="marzo" or mes=="mayo" or mes=="julio"or mes=="agosto"or mes=="octubre"or mes=="diciembre"):
  print("esta es una fecha valida")

else:
  print("Esta fecha no es valida")
