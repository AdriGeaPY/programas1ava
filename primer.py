dia=int(input("dime un dia del año"))
print("ahora dime un mes del año (letra) (en mayuscula NO)")
mes=input()
print("por ultimo, dime un año")
año=input()
año=int(año)
if dia <= 30 and ( mes =="enero"or mes=="marzo"or mes=="abril"or mes=="mayo"or mes=="junio"or mes=="julio"or mes=="agosto"or mes=="septiembre"or mes=="octubre"or mes=="noviembre"or mes=="diciembre"):
  print("esta fecha es correcta")
if dia > 30 and (mes != "febrero"or mes !="enero"or mes!="marzo"or mes!="abril"or mes!="mayo"or mes!="junio"or mes!="julio"or mes!="agosto"or mes!="septiembre"or mes!="octubre"or mes!="noviembre"or mes!="diciembre") : 
  print("esta no es una fecha valida")
if dia < 0 or año < 0:
  print("esta es una fecha valida")
if dia > 28 and (mes == "febrero"):
  print("esta fecha no es valida")
