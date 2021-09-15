l=[[],[],[],[],[]]
x=0
print("Ficha de ejemplo: Enrique, Iglesias, 12, 160, 45")
for i in range(2):
  a=input("Nombre: ")
  b= input("Apellido: ")
  c=(input("Años: "))
  d= (input("Estatura: "))
  e= (input("Peso: "))
  l[x].append(a); l[x].append(b) ; l[x].append(c); l[x].append(d); l[x].append(e)
  x=x+1
cuenta = " ".join(l[x])
g= cuenta.count("a")
u= cuenta.count("A")
t=g+u
n= cuenta.count("9")
print("Numero de ``aes´´: ", t)
print("Numero de nueves: ", n)
f=(input("Dime el nombre de la persona de quien quieres saber: "))
if f==l[a]:
  print(l[0])
elif f==b:
  print(l[1])