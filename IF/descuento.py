print("digame cuanto le ha costado su producto: ")
producto=input()
x=int(producto)
print("¿y cual es el precio original de su producto?")
original=input()
i=int(original)
c=i-x
a=x*100/i
b=round(100-a)
print("le han hecho una rebaja de: ", c,"€")
print("en porcentaje seria: ",b, "%")
if c < 0:
  print("no te has ahorrado nada")
if b<0:
  print("no hay porcentaje")