print("¿cuanto cuesta tu producto?")
producto=input()
producto=int(producto)
print("tu producto con IVA cuesta: ", producto*121 / 100)
print("tu producto costaba: ",producto, "y le he sumado el 21% de IVA,que es:", producto*21 /100)