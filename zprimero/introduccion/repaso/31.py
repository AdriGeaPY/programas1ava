def puntos(a,b):
  c= 0
  for i in a:
    if b == i:
      c = c + 1
  return c
texto = input("pon una oración")
signo = input("signo a contar")
print(puntos(texto,signo))
