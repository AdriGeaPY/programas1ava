while True: 
  grados=int(input("¿Cuantos grados hace hoy?: "))
  if grados < 0:
    print("Te tienes que poner un POLAR")
    break
  elif grados in range(0,9):
    print("Tienes que ponerte GUANTES Y BUFANDA")
    break
  elif grados in range(10,19):
    print("Tienes que ponerte MANGA CORTA")
    break
  elif grados in range (20,30):
    print("Tienes que ir en BAÑADOR")
    break
  elif grados not in range(-10,30):
    print("NO entiendo que estas poniendo")
    continue
