file = open("archivo.txt" , "r")
var=file.read()
print(var)
if var== "<!DOCTYPE html>" or var=="<!doctype html":
	print("Es un html")
else:
	print("no es un html")