while True:
	frases= input("Frases: ")
	fra=frases.split(".")
	space = frases.count("  ")
	for i in fra:
		pal=len(i.split(" "))
		c = pal-space
	print(c)
	if c >= 20:
		print("Has ganado")
		break