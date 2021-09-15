print("dime un primer numero: ")
numero1=input()
primer=int(numero1)
print("dime un segundo numero: ")
numero2=input()
segundo=int(numero2)
print("dime un tercer numero: ")
numero3=input()
tercer=int(numero3)
print("el orden creciente es: ")
if primer < segundo < tercer:
  print(primer,segundo,tercer)
if segundo < tercer < primer:
  print(segundo,tercer,primer)
if tercer < segundo < primer:
  print(tercer,segundo,primer)
if primer < tercer < segundo:
  print(primer,tercer,segundo)
if segundo < primer < tercer:
  print(segundo,primer,tercer)
if tercer < primer <segundo:
  print(tercer,primer,segundo)