l=[]
a=open('a1.txt','r')
for i in a:
	l.append(i)

b=open('a2.txt','r')
for y in b:
	print(y)
	l.append(y)

c=open('a3.txt','r')
for v in c:
	print(v)
	l.append(v)

print(l)