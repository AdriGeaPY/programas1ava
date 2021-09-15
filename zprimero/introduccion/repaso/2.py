def devolver(a):
  b= a.split()
  c = ""
  for i in b:
    c = c + i[0] + " "
  return c
texto = input("escribe una frase\n")
print(devolver(texto))