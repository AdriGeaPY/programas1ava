var=""
palabras=0
while True:
  var=var+input("Escribe un texto \n")
  if var!="":
    palabras=1
  for i in range(0,len(var)):
    print(i,var[i],var[i+1])
    if var[i]==" " and var[i+1]!=" " and var[i+2]!=" ":
      palabras=palabras+1
  if palabras>=20:
    break
  else:
    var=var+" "
    print("continua, llevas",palabras,"palabras",var)
    continue