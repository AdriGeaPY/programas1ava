
l = [1,2,3,4,5,5,3,6,7,8,9]
def eliminar(l):
	while True:
		if 3 in l:
			l.remove(3)
			print(l)
		elif 5 in l:
			l.remove(5)
			print(l)
		elif 7 in l:
			l.remove(7)
			print(l)
		else:
			break
	print(l)
eliminar(l)                                                                   
