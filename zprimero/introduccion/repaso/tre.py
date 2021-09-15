def OchoDigitos(var, i):
  if var[i] in Digitos and var[i+1] in Digitos and var[i+2] in Digitos and var[i+3] in Digitos and var[i+4] in Digitos and var[i+5] in Digitos and var[i+6] in Digitos and var[i+7] in Digitos and var[i+8] not in Digitos and var[i+8]!=" " and var[i+9]==" ":
    return True
  else:
    return False

var=input("Dato : ")
espia=False
Digitos=["0","1","2","3","4","5","6","7","8","9"]
for i in range(len(var)):
  if OchoDigitos(var,i):
    print("Sí hay un DNI")
    espia=True

if not espia:
  print ("No hemos encontrado ningún DNI")