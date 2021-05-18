archivo=input("dime el archivo que quieras abrir")
fichero=open(archivo+".txt","r")
b=fichero.read()
print(b)

def contar():
	contar=len