num=[[1,2,3]]
l=[]

for i in range(len(num)):
	print(num[i])

	suma=0

	for k in range(len(num[i])):
		suma=suma+num[i][k]
		l.append(suma)
print(l)

for x in range(len(l)):
	suma2=0
	suma2=suma2+l[x]
	print(suma2)

print("----------------------------------------------------------")

lista = [ [1, 2], [5, 4, 2], [12, 11, 120] ]
nume = 0

for i in lista:

    for m in i:
        nume += m
    print(i)    
    print(nume)

print("----------------------------------------------------------")

lista1 = [ [1, 2], [5, 4, 2], [12, 11, 120] ]
for l in lista1:
    print(sum(l))