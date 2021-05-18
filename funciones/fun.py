def Separar_Listas(listas):
	pares = []
	senar = []
	for i in listas:
		if i % 2 == 0:
			pares.append(i)
			pares.sort			
		elif i % 2 != 0:
			senar.append(i)
			senar.sort	
	return senar, pares

def entre(x,y):
	l=[]
	for i in range(x+1,y):
		l.append(i)
	return l

def eliminacion(lista):
	l=[]
	for i in l:
		l.remove(2)	#,l.remove(lista[4]),l.remove(lista[6])
	return l

def eliminar(l):
	l.pop(3)

	l.pop(4)
	
	l.pop(5)
	print(l)

def comparar(a,b):
	for i in a:
		for j in b:
			if i == j:
				return "cierto"
	return"falso"
	return a,b

#corregir texto
def checkUpper(text):
    nouText=text[0]
    #Codi per transformar a majúscules
    for pos in range(1,len(text)):
        if (text[pos-1] == "."):
            nouText=nouText+text[pos].upper()
        else:
            nouText=nouText+text[pos]
    return nouText

#rimas poesia
def rimaPoesia(poesia):
    text = "no té rima"
    numFrase = 0
    for frase in poesia:
        for pos in range(numFrase+1,len(poesia)):
            if frase[-3:].lower() == poesia[pos][-3:].lower() :
                print(frase)
                print(poesia[pos])
                return "té rima"
        numFrase = numFrase +1    
    return text