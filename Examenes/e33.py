import random
from random import randint
import random
nom = input("Entra el teu nom: ")
pri = input("Entra el teu primer cognom: ")
seg = input("Entra el teu segon cognom: ")

l=["@","#","!"]

usuari = ""
password=""

usuari= nom[0]+nom[1]+pri[0]+pri[len(pri)-1]+seg[len(seg)-2]+seg[len(seg)-1]


password= str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+ nom[0].upper() + pri[0].lower()

print("El teu usuari per accedir és "+usuari+" i el teu password "+ password)


#no me ha dado tiempo con la lista


