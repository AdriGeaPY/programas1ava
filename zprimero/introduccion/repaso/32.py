def puntos(a,b,c):
    k=0
    g=0
    while True:
        for i in a:
            if c == i:
                k=k+1
                continue
            elif c!=i:
                g=g+1
                continue
            elif g == b:
                break
    return "se repite ",k,"veces el caracter ",b

texto = input("pon una oracion: ")
signo = int (input("cuantos signos quieres contar: "))
caracter=input("que caracteres quieres: ")
print (puntos(texto,signo,caracter))