lista_alumnos=list()

#Introducción de datos
while True:
	nombre=input("Introduce nombre\n")
	apellido=input("Introduce apellido\n")
	edad=input("Introduce edad\n")
	altura=input("Introduce altura\n")
	peso=input("Introduce peso\n")
	lista_alumnos.append([nombre,apellido,edad,altura,peso])

	if len(lista_alumnos)>1:
		break

#Solicitar alumno
nombreAlumnoABuscar=input("Introduce el nombre del alumno del que deseas obtener información: \n")

alumno_encontrado=list()
espia=False

#Buscar en la lista_alumnos
for alumno in lista_alumnos:
	for dato_alumno in alumno:
		if dato_alumno==nombreAlumnoABuscar:
			alumno_encontrado=alumno
			espia=True
	

#Mostrar resultados
if espia:
	print(alumno_encontrado)
else:
	print("Ningún alumno se llama así")
