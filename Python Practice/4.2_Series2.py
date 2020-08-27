'''
Given two integers A and B. Print all numbers from A to B inclusively,
in increasing order, if A < B, or in decreasing order, if A ≥ B.
'''
a = int(input())
b = int(input())
s = "" 
if a < b:
  for x in range(a,b+1):
    s += str(x) + " "
else:
  print
  for x in range(a,b-1,-1):
    s += str(x) + " "
print(s)