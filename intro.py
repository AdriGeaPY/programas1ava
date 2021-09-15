nombre=input("¿Como te llamas?: ")
apellido=input("¿Cual es tu primer apellido?: ")
edad=int(input("¿Cual es tu edad?: "))

if edad > 10:
	print(apellido)
elif edad <= 10:
	print(nombre)