l=[]
fichero=open("a3.txt","r")
for i in fichero:
	for j in i:
		l.append(j)
print(l)