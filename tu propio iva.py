print("¿cuanto cuesta tu producto?")
producto=input()
producto=int(producto)
print("¿cuanto porcentaje de IVA?")
iva=input()
iva=int(iva)
print("tu producto con IVA cuesta: ", producto + producto*iva/100)
print("tu producto costaba: ",producto, "y le he sumado el", iva ,"% de IVA,que es:", producto*iva /100)