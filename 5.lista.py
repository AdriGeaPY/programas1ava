lista=[]
x=7
for i in range(6):
  x=x-1
  lista.append(int (input("La temperatura maxima hace "+ str (x) +" dias era de: ")))
  lista.append(int (input("La temperatura minima hace "+ str(x) +" dias era de: ")))
print("la temperatura media es de: ",round(sum(lista)/len(lista),2),"grados")
print("la temperatura mas baja es de:",min(lista),"grados" )
print("la temperatura mas alta es de:",max(lista),"grados")