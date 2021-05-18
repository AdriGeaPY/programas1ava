import random
from random import randint
import random
nom = input("Entra el teu nom: ")
pri = input("Entra el teu primer cognom: ")
seg = input("Entra el teu segon cognom: ")
random1=random.randint(0,9)
random2=random.randint(0,9)
random3=random.randint(0,9)
random4=random.randint(0,9)
usuari = ""
password=""

usuari= nom[0]+nom[1]+pri[0]+pri[len(pri)-1]+seg[len(seg)-2]+seg[len(seg)-1]


password= random1 + random2 + random3 + random4 + nom[0].upper()

print("El teu usuari per accedir és "+usuari+" i el teu password "+ password)


#Aquí heu de posar el vostre codi per obtenir l'usuari
#Recordeu usuari és les dues primeres lletres del nom, seguit de la
#primera i última lletra del primer cognom i les dues darreres lletres del
#segon cognom. Tot ha d'estar en minúscules.
 
#Aquí heu de posar el vostre codi per obtenir el password
#El password és quatre números aleatoris, la primera lletra del nom en
#majúscules, la primera lletra del primer cognom en minúcules i un caràcter
#aleatori de la llista de # @ !

