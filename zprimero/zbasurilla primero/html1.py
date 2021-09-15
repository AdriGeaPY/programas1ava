
while True:
  b = input("que numero?")
  f = open('a'+b+'.txt' , 'r')
  a = f.read()
  if a == "si":
    print(a)
    break
  else:
    print (a)