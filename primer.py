import calendar
dia=int(input("dime el dia: "))
mes=int(input("dime el mes: "))
año=int(input("dime el año: "))
if año <= 9999 and año >=1:
  if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia >=1 and dia <= 31:
      print("la fecha es correcta")
    else:
      print("la fecha no es correcta")
  elif mes == 4 or mes == 6 or mes== 9 or mes == 11:
    if dia >= 1 and dia <= 30:
      print("la fecha es correcta")
    else:
      print("la fecha no es correcta")
  elif calendar.isleap(año) and mes == 2:
    if dia >= 1 and dia <= 29:
      print("la fecha es correcta")
    else: 
      print("la fecha no es correcta")
