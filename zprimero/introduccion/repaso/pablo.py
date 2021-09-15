def dni(a):
	k=0
	q=0

	for i in a:
		if i==i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
			k=k+1
			if k == 8:
				q=q+1
				if q == 1:
					print("Hay un dni")
					return True
				else:
					return False
		elif i != "1" or i != "2" or i != "3" or i != "4" or i != "5" or i != "6" or i != "7" or i != "8" or i != "9":
			k = 0
		

serie=input("dime una serie de caracteres: ")
print(dni(serie))

# el unico fallo es que si pones mas de 8 numeros y una letra al final tambien lo cuenta

''''
if (i == "1" and letras) or (i == "2" and letras) or (i == "3" and letras) or (i and "4"and letras) or (i == "5" and letras) or (i == "6" and letras) or (i == "7" and letras) or (i == "8" and letras) or (i == "9" and letras):
'''
''''
i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9"
'''