lista=[]
for i in range(5):
  a=int(input("que has sacado?"))
  lista.append(a)
print("la nota mas alta: ",max(lista))
print("la nota minima: ",min(lista))
print("la media es: ", sum(lista)/len(lista))