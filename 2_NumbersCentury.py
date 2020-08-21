# Read an integer:
a = int(input())
next = True
if a%100 == 0:
  next = False
if a < 1000:
  amnt = 10
else:
  amnt = 100
while a > amnt:
  a = int(a/10)
if next == True:
  print (a+1)
else:
  print(a)

