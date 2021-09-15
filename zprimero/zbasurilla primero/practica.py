file = open('sencillo.txt', 'r').readlines()


countrylist = []

#turn into list and remove extra "
for i in file:
	i = i.replace('"', '')
	countrylist.append(i.split(','))


print(countrylist)

