import calendar
dia=int(input("dime el dia: "))
mes=int(input("dime el mes: "))
año=int(input("dime el año: "))
hora=int(input("dime la hora: "))
minuto=int(input("dime el minuto: "))
segundo=int(input("dime el segundo: "))
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
  elif not calendar.isleap(año) and mes == 2:
    if dia >= 1 and dia <= 28:
      print("la fecha es correcta")
    else:
      print("La fecha es incorrecta")
  else:
    print("ESTA MAL COMO TU VIDA")
else:
  print("ESTA MAL GILIPOLLAS HABER IDO AL COLEGIO")
if hora <= 24 and minuto < 60 and segundo < 60:
  if hora > 0 and minuto > 0 and segundo > 0:
    if segundo == 59:
      if minuto == 59:
        if hora == 23:
          if dia == 30:
            print("la fecha y hora será: ", 1, 0, 0, 0 )
          else:
            print("la fecha será:", dia+1, 0, 0, 0)
        else:
          print("la hora sera: ", hora+1, 0, 0)
      else:
        print("la hora será: ", hora, minuto+1,0)
    else:
      print("su hora con un segundo mas seria: ", hora,"h", minuto,"min", segundo+1,"seg",)
  else: 
    print("esta hora no es correcta")
else:
 print("la hora no es correcta")