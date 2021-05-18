x=list()
for i in range(5):
  y=list()
  for j in range(10):
    if i==0 or i==4:
      y.append("1")
    elif j==0 or j==9:
      y.append("1")
    else:
      y.append("0")
    x.append(y)
    print(y)
  for n in range 