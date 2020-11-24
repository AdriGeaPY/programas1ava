import random
a=(input("Hola, ¿como te llamas?: "))
print("Bien,",a," vamos a jugar a Lotto, procedo a darte una combinacion de 6 numeros aleatorios del 0 al 49: ")
x=0
while True:
	while x!=6:    
		b=random.randint(0,49)
		print(b,end=' ') 
		x=x+1
c=(input("\n¿Esta combinacion de numeros te gusta para jugar?: "))
if c=="si":
  print(a," ¡Espero que tengas mucha suerte en el juego!")
  c=(input("\n¿Esta combinacion de numeros te gusta para jugar?: "))
else:
  d=(input(" ¿Quieres volver a intentarlo?: "))
  if d=="si":
    print("venga")
    continue
  else:
    print("Esta bien, ",a," nos vemos.")
      break