'''
Given a three-digit integer X consisting of three different digits,
print "YES" if its three digits are going in an ascending order
from left to right and print "NO" otherwise.
'''
a = input()
tf=True
for x in range(len(a)-1):
  if a[x] > a[x+1]:
    tf = False
if tf:
  print("YES")
else:
  print("NO")
